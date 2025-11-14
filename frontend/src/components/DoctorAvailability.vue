<template>
    <div class="popup">
        <!-- Header Section -->
        <div class="header">
            <button class="back-btn" @click="$router.back()">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M19 12H5M12 19l-7-7 7-7"/>
                </svg>
                Back
            </button>
            <h2 class="title">Set Your Availability</h2>
            <p class="subtitle">Configure your schedule for the next 7 days</p>
        </div>

        <!-- Days List -->
        <div class="days-container">
            <div v-for="day in week" :key="day.date" class="day-card">
                <div class="day-header">
                    <div class="day-info">
                        <h3 class="day-title">{{ day.date }}</h3>
                        <span class="day-badge">{{ getDayName(day.date) }}</span>
                    </div>
                    <div class="fee-wrapper">
                        <span class="fee-label">Consultation Fee</span>
                        <div class="fee-input-wrapper">
                            <span class="currency">₹</span>
                            <input 
                                type="number" 
                                v-model="slotFee" 
                                placeholder="500" 
                                class="fee-input"
                            />
                        </div>
                    </div>
                </div>

                <div class="slots-section">
                    <h4 class="slots-title">Available Time Slots</h4>
                    <div class="slots-grid">
                        <button 
                            v-for="slot in slots" 
                            :key="slot.id" 
                            class="slot-button"
                            :class="{ active: isSelected(day.date, slot.id) }" 
                            @click="toggleSlot(day.date, slot.id)"
                        >
                            <svg v-if="isSelected(day.date, slot.id)" class="check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                                <polyline points="20 6 9 17 4 12"/>
                            </svg>
                            <span>{{ slot.label }}</span>
                        </button>
                    </div>
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
        },
        getDayName(date) {
            const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            const d = new Date(date);
            return days[d.getDay()];
        }
    }
}
</script>

<style scoped>
.popup {
    min-height: 100vh;
    background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
    padding: 24px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}

/* Header */
.header {
    max-width: 1000px;
    margin: 0 auto 32px;
}

.back-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    color: #475569;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    margin-bottom: 24px;
}

.back-btn:hover {
    background: #f8fafc;
    border-color: #cbd5e1;
    transform: translateX(-2px);
}

.title {
    font-size: 32px;
    font-weight: 700;
    color: #1e293b;
    margin: 0 0 8px;
    letter-spacing: -0.5px;
}

.subtitle {
    font-size: 16px;
    color: #64748b;
    margin: 0;
}

/* Days Container */
.days-container {
    max-width: 1000px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

/* Day Card */
.day-card {
    background: white;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
    transition: all 0.3s ease;
}

.day-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08), 0 2px 4px rgba(0, 0, 0, 0.05);
    transform: translateY(-2px);
}

/* Day Header */
.day-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 2px solid #f1f5f9;
    margin-bottom: 20px;
    flex-wrap: wrap;
    gap: 16px;
}

.day-info {
    display: flex;
    align-items: center;
    gap: 12px;
}

.day-title {
    font-size: 20px;
    font-weight: 600;
    color: #1e293b;
    margin: 0;
}

.day-badge {
    padding: 6px 14px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 500;
}

/* Fee Input */
.fee-wrapper {
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.fee-label {
    font-size: 12px;
    font-weight: 500;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.fee-input-wrapper {
    display: flex;
    align-items: center;
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 10px;
    padding: 0 14px;
    transition: all 0.2s ease;
}

.fee-input-wrapper:focus-within {
    border-color: #667eea;
    background: white;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.currency {
    font-size: 16px;
    font-weight: 600;
    color: #475569;
    margin-right: 4px;
}

.fee-input {
    border: none;
    background: transparent;
    padding: 10px 4px;
    font-size: 16px;
    font-weight: 600;
    color: #1e293b;
    width: 120px;
    outline: none;
}

.fee-input::placeholder {
    color: #94a3b8;
    font-weight: 400;
}

/* Slots Section */
.slots-section {
    margin-top: 20px;
}

.slots-title {
    font-size: 14px;
    font-weight: 600;
    color: #475569;
    margin: 0 0 14px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.slots-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 10px;
}

/* Slot Button */
.slot-button {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    padding: 14px 16px;
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 10px;
    color: #475569;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    overflow: hidden;
}

.slot-button::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    opacity: 0;
    transition: opacity 0.2s ease;
}

.slot-button span {
    position: relative;
    z-index: 1;
}

.check-icon {
    position: relative;
    z-index: 1;
}

.slot-button:hover {
    border-color: #cbd5e1;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
}

.slot-button.active {
    border-color: #667eea;
    color: white;
}

.slot-button.active::before {
    opacity: 1;
}

/* Footer */
.footer {
    max-width: 1000px;
    margin: 32px auto 0;
    display: flex;
    justify-content: flex-end;
}

.save-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 16px 32px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.save-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.save-btn:active {
    transform: translateY(0);
}

/* Responsive Design */
@media (max-width: 768px) {
    .popup {
        padding: 16px;
    }

    .title {
        font-size: 24px;
    }

    .day-header {
        flex-direction: column;
        align-items: flex-start;
    }

    .slots-grid {
        grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    }

    .save-btn {
        width: 100%;
        justify-content: center;
    }
}
</style>
