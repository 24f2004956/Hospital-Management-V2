<template>
  <div class="history-container">
    <div class="history-wrapper">
      
      <!-- Header Section -->
      <div class="page-header">
        <div class="header-content">
          <div class="header-icon">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14 2 14 8 20 8"/>
              <line x1="16" y1="13" x2="8" y2="13"/>
              <line x1="16" y1="17" x2="8" y2="17"/>
              <polyline points="10 9 9 9 8 9"/>
            </svg>
          </div>
          <div>
            <h1 class="page-title">Medical History</h1>
            <p class="page-subtitle" v-if="patient.name">{{ patient.name }}</p>
          </div>
        </div>
        <button class="export-button" @click="exportCSV">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <polyline points="7 10 12 15 17 10"/>
            <line x1="12" y1="15" x2="12" y2="3"/>
          </svg>
          Export CSV
        </button>
      </div>

      <!-- Records Section -->
      <div class="records-section">
        
        <!-- Empty State -->
        <div v-if="history.length === 0" class="empty-state">
          <div class="empty-icon">
            <svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14 2 14 8 20 8"/>
              <line x1="12" y1="18" x2="12" y2="12"/>
              <line x1="9" y1="15" x2="15" y2="15"/>
            </svg>
          </div>
          <h3 class="empty-title">No Medical Records</h3>
          <p class="empty-description">Your medical history will appear here once you have appointments.</p>
        </div>

        <!-- Records Grid -->
        <div v-else class="records-grid">
          <div v-for="(item, index) in history" :key="item.id" class="record-card">
            
            <!-- Card Header -->
            <div class="record-header">
              <div class="record-number">#{{ index + 1 }}</div>
              <div class="record-date">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                  <line x1="16" y1="2" x2="16" y2="6"/>
                  <line x1="8" y1="2" x2="8" y2="6"/>
                  <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
                {{ formatDate(item.date) }}
              </div>
            </div>

            <!-- Card Body -->
            <div class="record-body">
              
              <!-- Doctor Info -->
              <div class="info-row">
                <div class="info-icon doctor-icon">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                    <circle cx="12" cy="7" r="4"/>
                  </svg>
                </div>
                <div class="info-content">
                  <div class="info-label">Doctor</div>
                  <div class="info-value">{{ item.doctor_name }}</div>
                </div>
              </div>

              <!-- Department -->
              <div class="info-row">
                <div class="info-icon department-icon">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                    <polyline points="9 22 9 12 15 12 15 22"/>
                  </svg>
                </div>
                <div class="info-content">
                  <div class="info-label">Department</div>
                  <div class="info-value">{{ item.department_name }}</div>
                </div>
              </div>

              <!-- Diagnosis -->
              <div class="diagnosis-section">
                <div class="section-header">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
                  </svg>
                  Diagnosis
                </div>
                <div class="section-content">{{ item.diagnosis }}</div>
              </div>

              <!-- Prescription -->
              <div class="prescription-section">
                <div class="section-header">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                    <polyline points="14 2 14 8 20 8"/>
                    <line x1="16" y1="13" x2="8" y2="13"/>
                    <line x1="16" y1="17" x2="8" y2="17"/>
                  </svg>
                  Prescription
                </div>
                <div class="section-content">{{ item.prescription }}</div>
              </div>

              <!-- Medicines -->
              <div class="medicines-section">
                <div class="section-header">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <rect x="4" y="4" width="16" height="16" rx="2" ry="2"/>
                    <rect x="9" y="9" width="6" height="6"/>
                    <line x1="9" y1="1" x2="9" y2="4"/>
                    <line x1="15" y1="1" x2="15" y2="4"/>
                    <line x1="9" y1="20" x2="9" y2="23"/>
                    <line x1="15" y1="20" x2="15" y2="23"/>
                    <line x1="20" y1="9" x2="23" y2="9"/>
                    <line x1="20" y1="14" x2="23" y2="14"/>
                    <line x1="1" y1="9" x2="4" y2="9"/>
                    <line x1="1" y1="14" x2="4" y2="14"/>
                  </svg>
                  Medicines
                </div>
                <div class="section-content medicines-content">
                  {{ item.medicines || 'N/A' }}
                </div>
              </div>

            </div>
          </div>
        </div>

      </div>

      <!-- Back Button -->
      <div class="back-section">
        <router-link to="/patient-dashboard" class="back-button">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 12H5M12 19l-7-7 7-7"/>
          </svg>
          Back to Dashboard
        </router-link>
      </div>

    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      patient: {},
      history: [],
      message: "",
    };
  },

  async mounted() {
    const token = localStorage.getItem("patientToken");
    if (!token) return;

    // Fetch patient profile
    const profileResp = await fetch("/api/patient", {
      headers: { "Authorization": `Bearer ${token}` }
    });
    this.patient = await profileResp.json();

    // Fetch patient treatment history
    const historyResp = await fetch("/api/treatment/patient", {
      headers: { "Authorization": `Bearer ${token}` }
    });
    this.history = await historyResp.json();
  },

  methods: {
    formatDate(dateString) {
      if (!dateString) return "N/A";
      const date = new Date(dateString);
      return date.toISOString().slice(0, 10);
    },
    async exportCSV(){
        const token = localStorage.getItem("patientToken");
        if (!token) return;
    
        const response = await fetch("/api/treatment/export", {
            headers: { "Authorization": `Bearer ${token}` }
        });
        const result = await response.json();
    
        if (!response.ok) {
            alert("request failed");
            return;
        }else{
            alert(result.message);
        }
    }
  }
};
</script>

<style scoped>
.history-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 24px;
}

.history-wrapper {
  max-width: 1200px;
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

/* Header Section */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 32px;
  flex-wrap: wrap;
  gap: 16px;
}

.header-content {
  display: flex;
  align-items: center;
  gap: 16px;
}

.header-icon {
  width: 56px;
  height: 56px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.page-title {
  font-size: 32px;
  font-weight: 700;
  color: white;
  margin: 0;
  line-height: 1.2;
}

.page-subtitle {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.9);
  margin: 4px 0 0;
  font-weight: 500;
}

.export-button {
  background: rgba(255, 255, 255, 0.95);
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 600;
  color: #667eea;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.export-button:hover {
  background: white;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

/* Records Section */
.records-section {
  background: white;
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
  margin-bottom: 24px;
  min-height: 400px;
}

/* Empty State */
.empty-state {
  text-align: center;
  padding: 80px 24px;
  animation: slideUp 0.4s ease-out;
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

.empty-icon {
  margin: 0 auto 24px;
  color: #d1d5db;
}

.empty-title {
  font-size: 24px;
  font-weight: 700;
  color: #374151;
  margin: 0 0 8px;
}

.empty-description {
  font-size: 16px;
  color: #6b7280;
  margin: 0;
}

/* Records Grid */
.records-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 24px;
  animation: slideUp 0.4s ease-out;
}

.record-card {
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s;
}

.record-card:hover {
  border-color: #667eea;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
  transform: translateY(-4px);
}

.record-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 16px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
}

.record-number {
  font-size: 18px;
  font-weight: 700;
}

.record-date {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  font-weight: 500;
  opacity: 0.95;
}

.record-body {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.info-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
}

.info-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.doctor-icon {
  background: rgba(102, 126, 234, 0.1);
  color: #667eea;
}

.department-icon {
  background: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.info-content {
  flex: 1;
}

.info-label {
  font-size: 12px;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.info-value {
  font-size: 15px;
  font-weight: 600;
  color: #1f2937;
}

.diagnosis-section,
.prescription-section,
.medicines-section {
  padding: 16px;
  border-radius: 12px;
  background: #f9fafb;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 700;
  color: #374151;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 8px;
}

.section-header svg {
  color: #667eea;
}

.section-content {
  font-size: 14px;
  color: #4b5563;
  line-height: 1.6;
}

.medicines-content {
  font-weight: 500;
}

/* Back Section */
.back-section {
  text-align: center;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.95);
  color: #667eea;
  padding: 14px 28px;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.back-button:hover {
  background: white;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .history-container {
    padding: 16px;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .header-content {
    width: 100%;
  }

  .page-title {
    font-size: 24px;
  }

  .export-button {
    width: 100%;
    justify-content: center;
  }

  .records-section {
    padding: 20px;
  }

  .records-grid {
    grid-template-columns: 1fr;
  }

  .empty-state {
    padding: 60px 16px;
  }

  .empty-icon svg {
    width: 60px;
    height: 60px;
  }
}

@media (max-width: 480px) {
  .record-body {
    padding: 16px;
  }

  .info-icon {
    width: 32px;
    height: 32px;
  }

  .diagnosis-section,
  .prescription-section,
  .medicines-section {
    padding: 12px;
  }
}
</style>
