<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-container">
      <div class="modal-card">
        
        <!-- Header -->
        <div class="modal-header">
          <div>
            <h2 class="modal-title">Available Slots</h2>
            <p class="modal-subtitle">{{ doctor.name }}</p>
          </div>
          <button class="close-button" @click="$emit('close')" aria-label="Close">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M18 6L6 18M6 6l12 12"/>
            </svg>
          </button>
        </div>

        <!-- Body -->
        <div class="modal-body">
          <div v-if="groupedAvailability.length === 0" class="empty-state">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
              <line x1="16" y1="2" x2="16" y2="6"/>
              <line x1="8" y1="2" x2="8" y2="6"/>
              <line x1="3" y1="10" x2="21" y2="10"/>
            </svg>
            <h3>No Slots Available</h3>
            <p>This doctor doesn't have any available slots at the moment.</p>
          </div>

          <div v-else class="availability-list">
            <div v-for="day in groupedAvailability" :key="day.date" class="day-group">
              <div class="day-header">
                <span class="day-label">{{ day.date }}</span>
                <span class="slot-count">{{ day.slots.length }} slot{{ day.slots.length > 1 ? 's' : '' }}</span>
              </div>

              <div class="slots-grid">
                <button 
                  v-for="slot in day.slots" 
                  :key="slot.id" 
                  class="slot-button"
                  @click="goToPayment(day.date, slot)"
                >
                  <div class="slot-time">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <circle cx="12" cy="12" r="10"/>
                      <polyline points="12 6 12 12 16 14"/>
                    </svg>
                    <span>{{ slot.start_time.slice(0, 5) }} - {{ slot.end_time.slice(0, 5) }}</span>
                  </div>
                  <div class="slot-fee">
                    <span v-if="slot.fee && slot.fee > 0" class="fee-amount">₹{{ slot.fee }}</span>
                    <span v-else class="fee-free">Free</span>
                  </div>
                </button>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>


<script>
export default {
  props: ["doctor"],
  data() {
    return {
      availability: []
    };
  },
  computed: {
    groupedAvailability() {
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      const nextWeek = new Date();
      nextWeek.setDate(today.getDate() + 7);
      nextWeek.setHours(0, 0, 0, 0);

      const grouped = {};

      this.availability.forEach(slot => {
        const slotDate = new Date(slot.date + "T00:00:00");

        if (slotDate >= today && slotDate <= nextWeek) {
          if (!grouped[slot.date]) {
            grouped[slot.date] = { date: slot.date, slots: [] };
          }
          grouped[slot.date].slots.push(slot);
        }
      });

      const groupedArray = Object.values(grouped);

      groupedArray.sort((a, b) => new Date(a.date) - new Date(b.date));

      groupedArray.forEach(day => {
        day.slots.sort((a, b) => a.start_time.localeCompare(b.start_time));
      });

      return groupedArray;
    }



  },
  async mounted() {
    const token = localStorage.getItem("patientToken");
    const res = await fetch(`/api/availability?doctor_id=${this.doctor.id}`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    this.availability = await res.json();
  },
  methods: {
    goToPayment(date, slot) {
      this.$router.push({
        name: "PaymentScreen",
        query: {
          doctor_id: this.doctor.id,
          date,
          time: slot.start_time.slice(0, 5),
          fee: slot.fee
        }
      });
    },

    async book(date, time) {
      const token = localStorage.getItem("patientToken");

      const res = await fetch("/api/appointment", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          doctor_id: this.doctor.id,
          date,
          time,
          reason: "General Checkup"
        })
      });

      const data = await res.json();
      alert(data.message);
      this.$emit("close"); 
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.2s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.modal-container {
  width: 90%;
  max-width: 800px;
  max-height: 90vh;
  animation: slideUp 0.3s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-card {
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  max-height: 90vh;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 24px 28px;
  border-bottom: 1px solid #e5e7eb;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.modal-title {
  font-size: 24px;
  font-weight: 700;
  margin: 0;
  line-height: 1.2;
}

.modal-subtitle {
  font-size: 14px;
  margin: 4px 0 0;
  opacity: 0.95;
  font-weight: 500;
}

.close-button {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  color: white;
  flex-shrink: 0;
}

.close-button:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: scale(1.05);
}

.modal-body {
  padding: 24px 28px;
  overflow-y: auto;
  flex: 1;
}

.empty-state {
  text-align: center;
  padding: 48px 24px;
  color: #6b7280;
}

.empty-state svg {
  margin: 0 auto 20px;
  opacity: 0.3;
}

.empty-state h3 {
  font-size: 20px;
  font-weight: 600;
  margin: 0 0 8px;
  color: #374151;
}

.empty-state p {
  font-size: 15px;
  margin: 0;
  color: #9ca3af;
}

.availability-list {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.day-group {
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-10px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.day-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 2px solid #f3f4f6;
}

.day-label {
  font-size: 16px;
  font-weight: 700;
  color: #1f2937;
}

.slot-count {
  font-size: 13px;
  color: #6b7280;
  background: #f3f4f6;
  padding: 4px 12px;
  border-radius: 12px;
  font-weight: 500;
}

.slots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
}

.slot-button {
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  padding: 14px 16px;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: inherit;
  text-align: left;
}

.slot-button:hover {
  border-color: #667eea;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
}

.slot-button:active {
  transform: translateY(0);
}

.slot-time {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #374151;
  font-size: 14px;
  font-weight: 600;
}

.slot-time svg {
  color: #667eea;
  flex-shrink: 0;
}

.slot-fee {
  font-weight: 700;
  flex-shrink: 0;
}

.fee-amount {
  color: #667eea;
  font-size: 15px;
}

.fee-free {
  color: #10b981;
  font-size: 13px;
  background: #d1fae5;
  padding: 4px 10px;
  border-radius: 8px;
}

/* Scrollbar styling */
.modal-body::-webkit-scrollbar {
  width: 8px;
}

.modal-body::-webkit-scrollbar-track {
  background: #f3f4f6;
  border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 4px;
}

.modal-body::-webkit-scrollbar-thumb:hover {
  background: #9ca3af;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .modal-container {
    width: 95%;
  }

  .modal-header {
    padding: 20px;
  }

  .modal-title {
    font-size: 20px;
  }

  .modal-body {
    padding: 20px;
  }

  .slots-grid {
    grid-template-columns: 1fr;
  }

  .slot-button {
    padding: 12px 14px;
  }
}
</style>
