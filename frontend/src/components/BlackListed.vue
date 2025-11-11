<template>
  <!-- Modern Sidebar Navigation -->
  <div class="d-flex min-vh-100">
    <!-- Sidebar -->
    <nav class="sidebar bg-dark text-white d-flex flex-column p-3" style="width: 260px; position: fixed; height: 100vh; overflow-y: auto;">
      <div class="mb-4">
        <h4 class="fw-bold text-white mb-0">
          <i class="bi bi-hospital"></i> Admin Portal
        </h4>
        <small class="text-white-50">Healthcare Management</small>
      </div>

      <ul class="nav flex-column gap-2">
        <li class="nav-item">
          <router-link to="/admin-dashboard" class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight">
            <i class="bi bi-speedometer2 me-2"></i> Dashboard
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/create-department" class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight">
            <i class="bi bi-building me-2"></i> Create Department
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/doctor-register" class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight">
            <i class="bi bi-person-plus me-2"></i> Register Doctor
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/blacklisted" class="nav-link text-white rounded d-flex align-items-center py-2 px-3" 
                       style="background: rgba(255,255,255,0.1);">
            <i class="bi bi-shield-x me-2"></i> Blacklisted Records
          </router-link>
        </li>
        
        <hr class="border-white-50 my-3">
        
        <li class="nav-item">
          <a class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight" 
             href="#patient-section">
            <i class="bi bi-people me-2"></i> Patients
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight" 
             href="#doctor-section">
            <i class="bi bi-person-badge me-2"></i> Doctors
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight" 
             href="#department-section">
            <i class="bi bi-diagram-3 me-2"></i> Departments
          </a>
        </li>
      </ul>

      <div class="mt-auto pt-3 border-top border-white-50">
        <button class="btn btn-outline-danger w-100 d-flex align-items-center justify-content-center" @click="logout">
          <i class="bi bi-box-arrow-right me-2"></i> Logout
        </button>
      </div>
    </nav>

    <!-- Main Content Area -->
    <div class="flex-grow-1" style="margin-left: 260px; background: #f8f9fa;">
      <!-- Top Header Bar -->
      <header class="bg-white shadow-sm p-4 mb-4">
        <div class="container-fluid">
          <div class="d-flex justify-content-between align-items-center">
            <div>
              <h4 class="mb-1 fw-bold text-dark">
                <i class="bi bi-shield-x text-danger me-2"></i>Blacklisted Records
              </h4>
              <small class="text-muted">Manage restricted doctors and patients</small>
            </div>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb mb-0 bg-light px-3 py-2 rounded">
                <li class="breadcrumb-item">
                  <router-link to="/admin-dashboard" class="text-decoration-none">
                    <i class="bi bi-house-door me-1"></i>Dashboard
                  </router-link>
                </li>
                <li class="breadcrumb-item active">Blacklisted Records</li>
              </ol>
            </nav>
          </div>
        </div>
      </header>

      <!-- Main Content Container -->
      <div class="container-fluid px-4 pb-5">
        <!-- Stats Cards -->
        <div class="row g-3 mb-4">
          <div class="col-md-6">
            <div class="card border-0 shadow-sm h-100">
              <div class="card-body">
                <div class="d-flex align-items-center">
                  <div class="flex-shrink-0">
                    <div class="bg-danger bg-opacity-10 p-3 rounded">
                      <i class="bi bi-person-badge text-danger fs-3"></i>
                    </div>
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h6 class="text-muted mb-1">Blacklisted Doctors</h6>
                    <h3 class="mb-0 fw-bold">{{ blacklistedDoctors.length }}</h3>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card border-0 shadow-sm h-100">
              <div class="card-body">
                <div class="d-flex align-items-center">
                  <div class="flex-shrink-0">
                    <div class="bg-warning bg-opacity-10 p-3 rounded">
                      <i class="bi bi-people text-warning fs-3"></i>
                    </div>
                  </div>
                  <div class="flex-grow-1 ms-3">
                    <h6 class="text-muted mb-1">Blacklisted Patients</h6>
                    <h3 class="mb-0 fw-bold">{{ blacklistedPatients.length }}</h3>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Blacklisted Doctors Section -->
        <div class="card border-0 shadow-sm mb-4" id="doctor-section">
          <div class="card-header bg-white border-0 py-3">
            <div class="d-flex align-items-center">
              <div class="bg-danger bg-opacity-10 p-2 rounded me-3">
                <i class="bi bi-person-badge text-danger fs-5"></i>
              </div>
              <div>
                <h5 class="mb-0 fw-bold">Blacklisted Doctors</h5>
                <small class="text-muted">Medical professionals with restricted access</small>
              </div>
            </div>
          </div>
          <div class="card-body p-0">
            <div class="table-responsive">
              <table class="table table-hover mb-0">
                <thead class="table-light">
                  <tr>
                    <th class="px-4 py-3 text-muted fw-semibold" style="width: 60px;">#</th>
                    <th class="py-3 text-muted fw-semibold">Doctor Details</th>
                    <th class="py-3 text-muted fw-semibold">Contact Information</th>
                    <th class="py-3 text-muted fw-semibold">Department</th>
                    <th class="py-3 text-muted fw-semibold text-center">Experience</th>
                    <th class="py-3 text-muted fw-semibold text-center" style="width: 150px;">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(doctor, index) in blacklistedDoctors" :key="doctor.id" class="align-middle">
                    <td class="px-4">
                      <span class="badge bg-light text-dark">{{ index + 1 }}</span>
                    </td>
                    <td>
                      <div class="d-flex align-items-center">
                        <div class="bg-danger bg-opacity-10 rounded-circle p-2 me-3" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">
                          <i class="bi bi-person-fill text-danger"></i>
                        </div>
                        <div>
                          <div class="fw-semibold text-dark">{{ doctor.name }}</div>
                          <small class="text-muted">ID: #{{ doctor.id }}</small>
                        </div>
                      </div>
                    </td>
                    <td>
                      <div>
                        <div class="text-dark mb-1">
                          <i class="bi bi-envelope me-2 text-muted"></i>{{ doctor.email }}
                        </div>
                        <div class="text-muted small">
                          <i class="bi bi-telephone me-2"></i>{{ doctor.contact || 'Not provided' }}
                        </div>
                      </div>
                    </td>
                    <td>
                      <span class="badge bg-primary bg-opacity-10 text-primary px-3 py-2">
                        {{ doctor.department_name }}
                      </span>
                    </td>
                    <td class="text-center">
                      <span class="fw-semibold text-dark">{{ doctor.experience_years || 'N/A' }}</span>
                      <small class="text-muted d-block">years</small>
                    </td>
                    <td class="text-center">
                      <button class="btn btn-warning btn-sm shadow-sm" @click="unblacklistDoctor(doctor)">
                        <i class="bi bi-arrow-counterclockwise me-1"></i>
                        Restore
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div v-if="blacklistedDoctors.length === 0" class="text-center py-5">
              <div class="mb-3">
                <i class="bi bi-check-circle text-success" style="font-size: 3rem;"></i>
              </div>
              <h6 class="text-muted">No blacklisted doctors found</h6>
              <p class="text-muted small mb-0">All doctors are currently active</p>
            </div>
          </div>
        </div>

        <!-- Blacklisted Patients Section -->
        <div class="card border-0 shadow-sm" id="patient-section">
          <div class="card-header bg-white border-0 py-3">
            <div class="d-flex align-items-center">
              <div class="bg-warning bg-opacity-10 p-2 rounded me-3">
                <i class="bi bi-people text-warning fs-5"></i>
              </div>
              <div>
                <h5 class="mb-0 fw-bold">Blacklisted Patients</h5>
                <small class="text-muted">Patients with restricted access</small>
              </div>
            </div>
          </div>
          <div class="card-body p-0">
            <div class="table-responsive">
              <table class="table table-hover mb-0">
                <thead class="table-light">
                  <tr>
                    <th class="px-4 py-3 text-muted fw-semibold" style="width: 60px;">#</th>
                    <th class="py-3 text-muted fw-semibold">Patient Details</th>
                    <th class="py-3 text-muted fw-semibold">Email</th>
                    <th class="py-3 text-muted fw-semibold text-center">Age</th>
                    <th class="py-3 text-muted fw-semibold text-center">Gender</th>
                    <th class="py-3 text-muted fw-semibold text-center" style="width: 150px;">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(patient, index) in blacklistedPatients" :key="patient.id" class="align-middle">
                    <td class="px-4">
                      <span class="badge bg-light text-dark">{{ index + 1 }}</span>
                    </td>
                    <td>
                      <div class="d-flex align-items-center">
                        <div class="bg-warning bg-opacity-10 rounded-circle p-2 me-3" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">
                          <i class="bi bi-person-fill text-warning"></i>
                        </div>
                        <div>
                          <div class="fw-semibold text-dark">{{ patient.name }}</div>
                          <small class="text-muted">ID: #{{ patient.id }}</small>
                        </div>
                      </div>
                    </td>
                    <td>
                      <i class="bi bi-envelope me-2 text-muted"></i>
                      <span class="text-dark">{{ patient.email }}</span>
                    </td>
                    <td class="text-center">
                      <span class="badge bg-info bg-opacity-10 text-info">
                        {{ patient.age || 'N/A' }}
                      </span>
                    </td>
                    <td class="text-center">
                      <span class="badge" :class="patient.gender === 'Male' ? 'bg-primary bg-opacity-10 text-primary' : 'bg-danger bg-opacity-10 text-danger'">
                        <i class="bi" :class="patient.gender === 'Male' ? 'bi-gender-male' : 'bi-gender-female'"></i>
                        {{ patient.gender || 'N/A' }}
                      </span>
                    </td>
                    <td class="text-center">
                      <button class="btn btn-warning btn-sm shadow-sm" @click="unblacklistPatient(patient)">
                        <i class="bi bi-arrow-counterclockwise me-1"></i>
                        Restore
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div v-if="blacklistedPatients.length === 0" class="text-center py-5">
              <div class="mb-3">
                <i class="bi bi-check-circle text-success" style="font-size: 3rem;"></i>
              </div>
              <h6 class="text-muted">No blacklisted patients found</h6>
              <p class="text-muted small mb-0">All patients are currently active</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hover-highlight:hover {
  background: rgba(255, 255, 255, 0.1) !important;
  transition: background 0.3s ease;
}

.nav-link.router-link-active {
  background: rgba(255, 255, 255, 0.1);
}

.table > tbody > tr:hover {
  background-color: rgba(0, 0, 0, 0.02);
}

.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1) !important;
}

.btn {
  transition: all 0.2s ease;
}

.btn:hover {
  transform: translateY(-1px);
}

.badge {
  font-weight: 500;
}
</style>

<script>
export default {
  data() {
    return {
      doctors: [],
      patients: [],
    };
  },

  computed: {
    blacklistedDoctors() {
      return this.doctors.filter(d => d.black_list_status === 'active');
    },
    blacklistedPatients() {
      return this.patients.filter(p => p.black_list_status === 'active');
    }
  },

  methods: {
    async fetchDoctors() {
      const response = await fetch('/api/doctor', {
        headers: { 'Authorization': `Bearer ${localStorage.getItem('adminToken')}` }
      });
      this.doctors = await response.json();
    },

    async fetchPatients() {
      const response = await fetch('/api/patient', {
        headers: { 'Authorization': `Bearer ${localStorage.getItem('adminToken')}` }
      });
      this.patients = await response.json();
    },

    async unblacklistDoctor(doctor) {
      await this.updateStatus("doctor", doctor.id);
      this.fetchDoctors();
    },

    async unblacklistPatient(patient) {
      await this.updateStatus("patient", patient.id);
      this.fetchPatients();
    },

    async updateStatus(type, id) {
      const response = await fetch(`/api/account/${type}/${id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem('adminToken')}`
        },
        body: JSON.stringify({ status: "deactive" }) // Unblacklist
      });
      const result = await response.json();
      alert(result.message);
    }
  },

  mounted() {
    this.fetchDoctors();
    this.fetchPatients();
  }
};
</script>
