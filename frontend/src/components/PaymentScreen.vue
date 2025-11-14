<template>
  <div class="payment-container">
    <div class="payment-wrapper">
      
      <!-- Header -->
      <div class="page-header">
        <button class="back-button" @click="$router.back()" aria-label="Go back">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
        </button>
        <div>
          <h1 class="page-title">Confirm Appointment</h1>
          <p class="page-subtitle">Review details and complete payment</p>
        </div>
      </div>

      <!-- Payment Card -->
      <div class="payment-card">
        
        <!-- Doctor Info Section -->
        <div class="info-section">
          <div class="section-icon doctor-section">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
          </div>
          <div class="section-content">
            <div class="section-label">Doctor</div>
            <div class="section-value">{{ doctor.name }}</div>
          </div>
        </div>

        <div class="divider"></div>

        <!-- Appointment Details Grid -->
        <div class="details-grid">
          
          <!-- Date -->
          <div class="detail-item">
            <div class="detail-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                <line x1="16" y1="2" x2="16" y2="6"/>
                <line x1="8" y1="2" x2="8" y2="6"/>
                <line x1="3" y1="10" x2="21" y2="10"/>
              </svg>
            </div>
            <div>
              <div class="detail-label">Date</div>
              <div class="detail-value">{{ date }}</div>
            </div>
          </div>

          <!-- Time -->
          <div class="detail-item">
            <div class="detail-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/>
                <polyline points="12 6 12 12 16 14"/>
              </svg>
            </div>
            <div>
              <div class="detail-label">Time</div>
              <div class="detail-value">{{ time }}</div>
            </div>
          </div>

        </div>

        <div class="divider"></div>

        <!-- Amount Section -->
        <div class="amount-section">
          <div class="amount-label">Amount to Pay</div>
          <div class="amount-value">
            <span class="currency">₹</span>{{ fee }}
          </div>
        </div>

        <div class="divider"></div>

        <!-- Reason Section -->
        <div class="reason-section">
          <label class="reason-label">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14 2 14 8 20 8"/>
              <line x1="16" y1="13" x2="8" y2="13"/>
              <line x1="16" y1="17" x2="8" y2="17"/>
            </svg>
            Reason for Appointment
            <span class="required">*</span>
          </label>
          <textarea 
            class="reason-input" 
            v-model="reason" 
            placeholder="Please describe your health concerns or symptoms..."
            rows="4"
          ></textarea>
          <div class="char-count">{{ reason.length }}/500 characters</div>
        </div>

        <!-- Action Buttons -->
        <div class="action-buttons">
          <button class="btn btn-primary" @click="confirmPayment">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="1" y="4" width="22" height="16" rx="2" ry="2"/>
              <line x1="1" y1="10" x2="23" y2="10"/>
            </svg>
            Pay ₹{{ fee }} & Confirm
          </button>
          <button class="btn btn-secondary" @click="$router.back()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18"/>
              <line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
            Cancel
          </button>
        </div>

        <!-- Security Note -->
        <div class="security-note">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          <span>Your payment is secure and encrypted</span>
        </div>

      </div>

      <!-- Payment Methods Info -->
      <div class="payment-methods">
        <div class="methods-label">Accepted Payment Methods</div>
        <div class="methods-icons">
          <div class="method-badge">Card</div>
          <div class="method-badge">UPI</div>
          <div class="method-badge">Net Banking</div>
          <div class="method-badge">Wallet</div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      doctor: {},
      date: this.$route.query.date,
      time: this.$route.query.time,
      fee: this.$route.query.fee,
      doctor_id: this.$route.query.doctor_id,
      reason: ""
    };
  },
  async mounted() {
  const token = localStorage.getItem("patientToken");
  const res = await fetch(`/api/doctor-details/${this.doctor_id}`, {
    headers: { Authorization: `Bearer ${token}` }
  });


  this.doctor = await res.json();
},

  methods: {
    async confirmPayment() {
      const token = localStorage.getItem("patientToken");
      const res = await fetch("/api/appointment", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          doctor_id: this.doctor_id,
          date: this.date,
          time: this.time,
          reason: this.reason,
          payment_status: "paid"
        })
      });

      const data = await res.json();
      alert(data.message);
      this.$router.push("/patient-dashboard");
    }
  }
};
</script>

<style scoped>
.payment-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 24px;
}

.payment-wrapper {
  max-width: 600px;
  margin: 0 auto;
  animation: fadeIn 0.4s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Header */
.page-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.back-button {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
  color: white;
  backdrop-filter: blur(10px);
  flex-shrink: 0;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateX(-4px);
}

.page-title {
  font-size: 28px;
  font-weight: 700;
  color: white;
  margin: 0;
  line-height: 1.2;
}

.page-subtitle {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.9);
  margin: 4px 0 0;
}

/* Payment Card */
.payment-card {
  background: white;
  border-radius: 20px;
  padding: 28px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
  animation: slideUp 0.4s ease-out;
  margin-bottom: 20px;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Info Section */
.info-section {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 20px;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  border-radius: 16px;
}

.section-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.doctor-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.section-content {
  flex: 1;
}

.section-label {
  font-size: 12px;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.section-value {
  font-size: 20px;
  font-weight: 700;
  color: #1f2937;
}

/* Divider */
.divider {
  height: 1px;
  background: linear-gradient(to right, transparent, #e5e7eb, transparent);
  margin: 24px 0;
}

/* Details Grid */
.details-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  background: #f9fafb;
  border-radius: 12px;
}

.detail-icon {
  width: 40px;
  height: 40px;
  background: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #667eea;
  flex-shrink: 0;
}

.detail-label {
  font-size: 12px;
  font-weight: 600;
  color: #6b7280;
  margin-bottom: 4px;
}

.detail-value {
  font-size: 15px;
  font-weight: 600;
  color: #1f2937;
}

/* Amount Section */
.amount-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.1) 100%);
  border-radius: 16px;
}

.amount-label {
  font-size: 15px;
  font-weight: 600;
  color: #374151;
}

.amount-value {
  font-size: 32px;
  font-weight: 800;
  color: #10b981;
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.currency {
  font-size: 24px;
}

/* Reason Section */
.reason-section {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.reason-label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  display: flex;
  align-items: center;
  gap: 8px;
}

.reason-label svg {
  color: #667eea;
}

.required {
  color: #ef4444;
}

.reason-input {
  padding: 14px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 15px;
  font-family: inherit;
  resize: vertical;
  transition: all 0.2s;
  background: white;
  line-height: 1.6;
}

.reason-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.reason-input::placeholder {
  color: #9ca3af;
}

.char-count {
  font-size: 12px;
  color: #9ca3af;
  text-align: right;
}

/* Action Buttons */
.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 24px;
}

.btn {
  padding: 16px 24px;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-family: inherit;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background: #f3f4f6;
  color: #374151;
}

.btn-secondary:hover {
  background: #e5e7eb;
  transform: translateY(-2px);
}

.btn:active {
  transform: translateY(0);
}

/* Security Note */
.security-note {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  background: #f0fdf4;
  border-radius: 10px;
  margin-top: 16px;
  font-size: 13px;
  font-weight: 500;
  color: #166534;
}

.security-note svg {
  color: #10b981;
  flex-shrink: 0;
}

/* Payment Methods */
.payment-methods {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 20px;
  text-align: center;
}

.methods-label {
  font-size: 13px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.methods-icons {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

.method-badge {
  background: rgba(255, 255, 255, 0.95);
  color: #667eea;
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .payment-container {
    padding: 16px;
  }

  .page-title {
    font-size: 24px;
  }

  .payment-card {
    padding: 20px;
  }

  .details-grid {
    grid-template-columns: 1fr;
  }

  .amount-value {
    font-size: 28px;
  }

  .currency {
    font-size: 20px;
  }

  .section-value {
    font-size: 18px;
  }
}

@media (max-width: 480px) {
  .info-section {
    padding: 16px;
  }

  .section-icon {
    width: 48px;
    height: 48px;
  }
}
</style>
