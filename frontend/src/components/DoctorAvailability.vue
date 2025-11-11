<template>
    <div class="popup">
        <button class="back-btn" @click="$router.back()">← Back</button>

        <h2 class="title">Set Availability (Next 7 Days)</h2>

        <div v-for="day in week" :key="day.date" class="day-row">
            <h3 class="day-title">{{ day.date }}</h3>

            <input type="number" v-model="slotFee" placeholder="Enter Fee (₹)" class="fee-input" />

            <div class="slots">
                <div v-for="slot in slots" :key="slot.id" class="slot-button"
                    :class="{ active: isSelected(day.date, slot.id) }" @click="toggleSlot(day.date, slot.id)">
                    {{ slot.label }}
                </div>
            </div>
        </div>
    </div>
</template>


<script>
const SLOT_MAP = {
    "07:30:00-09:30:00": 1,
    "10:00:00-12:00:00": 2,
    "14:30:00-16:30:00": 3,
    "17:00:00-19:00:00": 4,
    "20:30:00-21:30:00": 5
};

export default {
    data() {
        return {
            week: [],
            slots: [
                { id: 1, label: "7:30 - 9:30 AM" },
                { id: 2, label: "10:00 - 12:00 PM" },
                { id: 3, label: "2:30 - 4:30 PM" },
                { id: 4, label: "5:00 - 7:00 PM" },
                { id: 5, label: "8:30 - 9:30 PM" },
            ],
            selectedSlots: [],
            slotFee: 0 
        }
    },

    mounted() {
        this.fetchWeek();
        this.fetchExisting();
    },

    methods: {
        fetchWeek() {
            const today = new Date();
            for (let i = 0; i < 7; i++) {
                const d = new Date(today);
                d.setDate(today.getDate() + i);
                this.week.push({ date: d.toISOString().slice(0, 10) });
            }
        },

        async fetchExisting() {
            const response = await fetch(`/api/availability-week`, {
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("doctorToken"),
                    "Content-Type": "application/json"
                }
            });

            const data = await response.json();
            this.selectedSlots = data;
        },

        isSelected(date, slotId) {
            return this.selectedSlots.some(s => {
                const key = `${s.start_time}-${s.end_time}`;
                const mappedSlot = SLOT_MAP[key];
                return s.date === date && mappedSlot === slotId;
            });
        },

        async toggleSlot(date, slotId) {
            await fetch("/api/availability-week", {
                method: "POST",
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("doctorToken"),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ date, slot_id: slotId, fee: this.slotFee })
            });

            this.fetchExisting();
        }
    }
}
</script>

<style>
.popup {
    padding: 20px;
    border-radius: 12px;
    background: #ffffff;
    max-width: 600px;
    margin: auto;
    box-shadow: 0 0 12px rgba(0, 0, 0, 0.1);
}

.title {
    text-align: center;
    margin-bottom: 16px;
    font-weight: 600;
    font-size: 20px;
}

.day-row {
    margin-bottom: 20px;
}

.day-title {
    margin-bottom: 8px;
    font-size: 16px;
    font-weight: 500;
}

.slots {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.slot-button {
    padding: 8px 14px;
    border: 1px solid #ccc;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.2s;
    background: #f7f7f7;
}

.slot-button:hover {
    background: #e8e8e8;
}

.slot-button.active {
    background: #0066ff;
    border-color: #004bcc;
    color: white;
}
.fee-input {
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    margin-bottom: 10px;
    width: 150px;
}

</style>
