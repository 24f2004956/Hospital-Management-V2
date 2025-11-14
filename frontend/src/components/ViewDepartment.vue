<template>
  <!-- Modern Navigation -->
  <nav class="modern-navbar">
    <div class="navbar-container">
      <div class="navbar-brand">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
        </svg>
        <span>Patient Portal</span>
      </div>

      <button class="mobile-toggle" @click="mobileMenuOpen = !mobileMenuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <div class="navbar-menu" :class="{ 'is-active': mobileMenuOpen }">
        <router-link to="/patient-dashboard" class="nav-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
            <polyline points="9 22 9 12 15 12 15 22"/>
          </svg>
          Home
        </router-link>

        <router-link to="/patient-profile-update" class="nav-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
            <circle cx="12" cy="7" r="4"/>
          </svg>
         Edit Profile
        </router-link>

        <router-link to="/history-export" class="nav-link">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 20h9"/>
            <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
          </svg>
          History
        </router-link>

        <button class="nav-link logout-btn" @click="logout">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
            <polyline points="16 17 21 12 16 7"/>
            <line x1="21" y1="12" x2="9" y2="12"/>
          </svg>
          Logout
        </button>
      </div>
    </div>
  </nav>

  <!-- Main Content -->
  <div class="department-content">
    <!-- Back Button -->
    <div class="back-section">
      <button class="back-btn" @click="$router.back()">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M19 12H5M12 19l-7-7 7-7"/>
        </svg>
        Back
      </button>
    </div>

    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Loading department information...</p>
    </div>

    <!-- Department Info & Doctors -->
    <div v-else-if="department" class="department-section">
      <!-- Department Header -->
      <div class="department-header">
        <div class="department-icon">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
          </svg>
        </div>
        <div class="department-info">
          <h1>{{ department.name }}</h1>
          <p>{{ department.description }}</p>
        </div>
      </div>

      <!-- Doctors Section -->
      <div class="doctors-section">
        <div class="section-header">
          <h2>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
              <circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
            </svg>
            Available Doctors
          </h2>
          <span class="badge">{{ doctors.length }} Doctors</span>
        </div>

        <!-- Doctors Grid -->
        <div class="doctors-grid">
          <div 
            v-for="(doctor, index) in doctors" 
            :key="doctor.id"
            class="doctor-card"
          >
            <div class="doctor-avatar">
              <span>{{ doctor.name.charAt(0).toUpperCase() }}</span>
            </div>
            
            <div class="doctor-info">
              <h3>Dr. {{ doctor.name }}</h3>
              <div class="doctor-meta">
              </div>
            </div>

            <div class="doctor-actions">
              <button class="action-btn view-btn" @click="viewDoctor(doctor)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/>
                  <circle cx="12" cy="12" r="3"/>
                </svg>
                View Profile
              </button>
              <button class="action-btn availability-btn" @click="checkAvailability(doctor)">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                  <line x1="16" y1="2" x2="16" y2="6"/>
                  <line x1="8" y1="2" x2="8" y2="6"/>
                  <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
                Check Availability
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="empty-state">
      <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
        <circle cx="12" cy="12" r="10"/>
        <line x1="12" y1="8" x2="12" y2="12"/>
        <line x1="12" y1="16" x2="12.01" y2="16"/>
      </svg>
      <h3>No Data Found</h3>
      <p>We couldn't find any information for this department.</p>
    </div>

    <!-- Modals -->
    <DoctorProfileModal 
      v-if="showProfileModal" 
      :doctor="selectedDoctor" 
      @close="showProfileModal = false" 
    />

    <AvailabilityModal 
      v-if="showAvailabilityModal" 
      :doctor="selectedDoctor" 
      @close="showAvailabilityModal = false" 
    />
  </div>
</template>




<script>
import DoctorProfileModal from "./DoctorProfileModal.vue";
import AvailabilityModal from "./AvailabilityModal.vue";

export default {
  name: "ViewDepartment",
  components: { DoctorProfileModal, AvailabilityModal },

  data() {
    return {
      department: null,
      doctors: [],
      loading: true,
      selectedDoctor: null,
      showProfileModal: false,
      showAvailabilityModal: false
    };
  },

  async mounted() {
    const departmentId = this.$route.params.id;

    try {
      const res = await fetch(`/api/department/${departmentId}`, {
        headers: { "Authorization": `Bearer ${localStorage.getItem("patientToken")}` }
      });

      const data = await res.json();

      if (res.ok) {
        this.department = data;
        this.doctors = data.doctors;
      }
    } catch {
      alert("Server error while loading department.");
    } finally {
      this.loading = false;
    }
  },

  methods: {
    async viewDoctor(doctor) {
      const res = await fetch(`/api/doctor-details/${doctor.id}`, {
        headers: { "Authorization": `Bearer ${localStorage.getItem("patientToken")}` }
      });

      this.selectedDoctor = await res.json();
      this.showProfileModal = true;
    },

    checkAvailability(doctor) {
      this.selectedDoctor = doctor;
      this.showAvailabilityModal = true;
    },
    logout() {
            localStorage.removeItem('patientToken');
            this.$router.push('/');
        },
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Modern Navigation */
.modern-navbar {
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: sticky;
  top: 0;
  z-index: 1000;
  border-bottom: 1px solid #e5e7eb;
}

.navbar-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 70px;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 20px;
  font-weight: 700;
  color: #1e293b;
}

.navbar-brand svg {
  color: #667eea;
}

.mobile-toggle {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
}

.mobile-toggle span {
  width: 24px;
  height: 2px;
  background: #64748b;
  border-radius: 2px;
  transition: all 0.3s ease;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 10px 16px;
  color: #64748b;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  border-radius: 8px;
  transition: all 0.2s ease;
  border: none;
  background: transparent;
  cursor: pointer;
}

.nav-link:hover {
  background: #f1f5f9;
  color: #1e293b;
}

.logout-btn {
  color: #ef4444;
}

.logout-btn:hover {
  background: #fef2f2;
  color: #dc2626;
}

/* Main Content */
.department-content {
  max-width: 1400px;
  margin: 0 auto;
  padding: 32px 24px;
  min-height: calc(100vh - 70px);
  background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
}

/* Back Section */
.back-section {
  margin-bottom: 24px;
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
}

.back-btn:hover {
  background: #f8fafc;
  border-color: #cbd5e1;
  transform: translateX(-2px);
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 80px 20px;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.spinner {
  width: 48px;
  height: 48px;
  border: 4px solid #e5e7eb;
  border-top-color: #667eea;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.loading-state p {
  color: #64748b;
  font-size: 16px;
  font-weight: 500;
}

/* Department Section */
.department-section {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* Department Header */
.department-header {
  background: white;
  padding: 40px;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  display: flex;
  align-items: center;
  gap: 24px;
}

.department-icon {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.department-icon svg {
  color: white;
}

.department-info h1 {
  font-size: 32px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 8px;
}

.department-info p {
  font-size: 16px;
  color: #64748b;
  line-height: 1.6;
}

/* Doctors Section */
.doctors-section {
  background: white;
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f1f5f9;
}

.section-header h2 {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 24px;
  font-weight: 700;
  color: #1e293b;
}

.badge {
  padding: 6px 14px;
  background: #667eea;
  color: white;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

/* Doctors Grid */
.doctors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 20px;
}

.doctor-card {
  background: #f8fafc;
  padding: 24px;
  border-radius: 12px;
  border: 2px solid #e2e8f0;
  transition: all 0.3s ease;
}

.doctor-card:hover {
  border-color: #667eea;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
  transform: translateY(-4px);
}

.doctor-avatar {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}

.doctor-avatar span {
  color: white;
  font-size: 24px;
  font-weight: 700;
}

.doctor-info h3 {
  font-size: 20px;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 8px;
}

.doctor-meta {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.experience {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #64748b;
  font-size: 14px;
  font-weight: 500;
}

.experience svg {
  color: #667eea;
}

.doctor-actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid transparent;
}

.view-btn {
  background: white;
  border-color: #e2e8f0;
  color: #475569;
}

.view-btn:hover {
  background: #f8fafc;
  border-color: #cbd5e1;
}

.availability-btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
}

.availability-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

/* Empty State */
.empty-state {
  background: white;
  padding: 80px 40px;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.empty-state svg {
  color: #cbd5e1;
  margin-bottom: 20px;
}

.empty-state h3 {
  font-size: 20px;
  font-weight: 600;
  color: #475569;
  margin-bottom: 8px;
}

.empty-state p {
  color: #94a3b8;
  font-size: 14px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .mobile-toggle {
    display: flex;
  }

  .navbar-menu {
    position: fixed;
    top: 70px;
    left: -100%;
    width: 280px;
    height: calc(100vh - 70px);
    background: white;
    flex-direction: column;
    align-items: flex-start;
    padding: 24px;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
    transition: left 0.3s ease;
  }

  .navbar-menu.is-active {
    left: 0;
  }

  .nav-link {
    width: 100%;
    justify-content: flex-start;
  }

  .department-header {
    flex-direction: column;
    text-align: center;
    padding: 24px;
  }

  .department-info h1 {
    font-size: 24px;
  }

  .doctors-grid {
    grid-template-columns: 1fr;
  }

  .section-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }
}
</style>