<template>
  <div class="profile-container">
    <div class="profile-wrapper">

      <!-- Header -->
      <div class="profile-header">
        <button class="back-button" @click="$router.back()" aria-label="Go back">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M19 12H5M12 19l-7-7 7-7" />
          </svg>
        </button>
        <div>
          <h1 class="page-title">Edit Profile</h1>
          <p class="page-subtitle">Update your personal information</p>
        </div>
      </div>

      <!-- Profile Card -->
      <div v-if="patient" class="profile-card">



        <!-- Form Fields -->
        <div class="form-grid">

          <!-- Name Field -->
          <div class="form-group">
            <label class="form-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                <circle cx="12" cy="7" r="4" />
              </svg>
              Full Name
            </label>
            <input v-model="patient.name" type="text" class="form-input" placeholder="Enter your full name" />
          </div>

          <!-- Email Field -->
          <div class="form-group">
            <label class="form-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                <polyline points="22,6 12,13 2,6" />
              </svg>
              Email Address
            </label>
            <input v-model="patient.email" type="email" class="form-input" placeholder="your.email@example.com" />
          </div>

          <!-- Gender Field -->
          <div class="form-group">
            <label class="form-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10" />
                <path d="M12 6v6l4 2" />
              </svg>
              Gender
            </label>
            <div class="gender-options">
              <label v-for="option in ['Male', 'Female', 'Other']" :key="option" class="gender-option"
                :class="{ active: patient.gender === option }">
                <input type="radio" :value="option" v-model="patient.gender" class="gender-radio" />
                <span class="gender-label">{{ option }}</span>
              </label>
            </div>
          </div>

          <!-- Age Field -->
          <div class="form-group">
            <label class="form-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
                <line x1="16" y1="2" x2="16" y2="6" />
                <line x1="8" y1="2" x2="8" y2="6" />
                <line x1="3" y1="10" x2="21" y2="10" />
              </svg>
              Age (Years)
            </label>
            <input v-model="patient.age" type="number" class="form-input" placeholder="Enter your age" min="0"
              max="150" />
          </div>

          <!-- Address Field -->
          <div class="form-group">
            <label class="form-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 6-9 12-9 12S3 16 3 10a9 9 0 0 1 18 0z" />
                <circle cx="12" cy="10" r="3" />
              </svg>

              Address
            </label>
            <input v-model="patient.address" type="email" class="form-input"
              placeholder="Vill- Diwanganj , PO- Rautara , Bihar" />
          </div>

          <!-- Contact Field -->
          <div class="form-group">
            <label class="form-label">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round">
                <path
                  d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.79 19.79 0 0 1 2.08 4.18 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.72c.12.9.38 1.78.76 2.6a2 2 0 0 1-.45 2.11L9.91 9.91a16 16 0 0 0 6 6l1.48-1.48a2 2 0 0 1 2.11-.45c.82.38 1.7.64 2.6.76A2 2 0 0 1 22 16.92z" />
              </svg>

              Contact
            </label>
            <input v-model="patient.contact" type="email" class="form-input" placeholder="Enter your contact details" />
          </div>

        </div>

        <!-- Action Buttons -->
        <div class="action-buttons">
          <button class="btn btn-secondary" @click="$router.back()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
            Cancel
          </button>
          <button class="btn btn-primary" @click="updateProfile">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="20 6 9 17 4 12" />
            </svg>
            Save Changes
          </button>
        </div>

      </div>

      <!-- Loading State -->
      <div v-else class="loading-state">
        <div class="spinner"></div>
        <p>Loading profile...</p>
      </div>

    </div>
  </div>
</template>


<script>
export default {
  data() {
    return { patient: null };
  },

  async mounted() {
    const res = await fetch("/api/patient", {
      headers: { Authorization: "Bearer " + localStorage.getItem("patientToken") }
    });
    this.patient = await res.json();
  },

  methods: {
    async updateProfile() {
      const res = await fetch(`/api/patient/profile-update`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + localStorage.getItem("patientToken")
        },
        body: JSON.stringify(this.patient)
      });

      const result = await res.json();
      alert(result.message);

      if (res.ok) this.$router.push("/patient-dashboard");
    }
  }
};
</script>


<style scoped>
.profile-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 24px;
}

.profile-wrapper {
  max-width: 800px;
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

.profile-header {
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
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateX(-4px);
}

.page-title {
  font-size: 32px;
  font-weight: 700;
  color: white;
  margin: 0;
  line-height: 1.2;
}

.page-subtitle {
  font-size: 15px;
  color: rgba(255, 255, 255, 0.9);
  margin: 4px 0 0;
}

.profile-card {
  background: white;
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
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

.avatar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  margin-bottom: 32px;
  padding-bottom: 32px;
  border-bottom: 2px solid #f3f4f6;
}

.avatar-circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
}

.change-photo-btn {
  background: #f3f4f6;
  border: none;
  padding: 10px 20px;
  border-radius: 10px;
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
}

.change-photo-btn:hover {
  background: #e5e7eb;
  transform: translateY(-2px);
}

.form-grid {
  display: grid;
  gap: 24px;
  margin-bottom: 32px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-size: 14px;
  font-weight: 600;
  color: #374151;
  display: flex;
  align-items: center;
  gap: 8px;
}

.form-label svg {
  color: #667eea;
}

.form-input {
  padding: 14px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 15px;
  font-family: inherit;
  transition: all 0.2s;
  background: white;
}

.form-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.form-input::placeholder {
  color: #9ca3af;
}

.gender-options {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

.gender-option {
  position: relative;
  cursor: pointer;
}

.gender-radio {
  position: absolute;
  opacity: 0;
}

.gender-label {
  display: block;
  padding: 14px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  text-align: center;
  font-size: 14px;
  font-weight: 600;
  color: #6b7280;
  transition: all 0.2s;
  background: white;
}

.gender-option:hover .gender-label {
  border-color: #667eea;
  background: rgba(102, 126, 234, 0.05);
}

.gender-option.active .gender-label {
  border-color: #667eea;
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  color: #667eea;
}

.action-buttons {
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}

.btn {
  padding: 14px 28px;
  border: none;
  border-radius: 12px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: inherit;
}

.btn-secondary {
  background: #f3f4f6;
  color: #374151;
}

.btn-secondary:hover {
  background: #e5e7eb;
  transform: translateY(-2px);
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

.btn:active {
  transform: translateY(0);
}

.loading-state {
  text-align: center;
  padding: 64px 24px;
  color: white;
}

.spinner {
  width: 48px;
  height: 48px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  margin: 0 auto 16px;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading-state p {
  font-size: 16px;
  margin: 0;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .profile-container {
    padding: 16px;
  }

  .page-title {
    font-size: 24px;
  }

  .profile-card {
    padding: 24px;
  }

  .avatar-circle {
    width: 100px;
    height: 100px;
  }

  .avatar-circle svg {
    width: 40px;
    height: 40px;
  }

  .gender-options {
    grid-template-columns: 1fr;
  }

  .action-buttons {
    flex-direction: column;
  }

  .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
