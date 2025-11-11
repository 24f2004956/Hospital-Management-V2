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
          <router-link to="/doctor-register" class="nav-link text-white rounded d-flex align-items-center py-2 px-3" 
                       style="background: rgba(255,255,255,0.1);">
            <i class="bi bi-person-plus me-2"></i> Register Doctor
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/blacklisted" class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight">
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
      <header class="bg-white shadow-sm p-3 mb-4">
        <div class="d-flex justify-content-between align-items-center">
          <div>
            <h5 class="mb-0 fw-bold text-dark">Register New Doctor</h5>
            <small class="text-muted">Add a new medical professional to your system</small>
          </div>
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mb-0">
              <li class="breadcrumb-item">
                <router-link to="/admin-dashboard" class="text-decoration-none">Dashboard</router-link>
              </li>
              <li class="breadcrumb-item active">Register Doctor</li>
            </ol>
          </nav>
        </div>
      </header>

      <!-- Content Container -->
      <div class="container-fluid px-4 pb-4">
        <div class="row justify-content-center">
          <div class="col-lg-8 col-xl-7">
            <!-- Form Card -->
            <div class="card border-0 shadow-sm">
              <div class="card-body p-4">
                <div class="d-flex align-items-center mb-4">
                  <div class="bg-success bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center me-3" 
                       style="width: 50px; height: 50px;">
                    <i class="bi bi-person-badge text-success fs-4"></i>
                  </div>
                  <div>
                    <h5 class="mb-0 fw-bold">Doctor Information</h5>
                    <small class="text-muted">Complete all fields to register a new doctor</small>
                  </div>
                </div>

                <form @submit.prevent="registerDoctor">
                  <!-- Name Field -->
                  <div class="mb-4">
                    <label for="name" class="form-label fw-semibold">
                      <i class="bi bi-person me-1 text-success"></i> Full Name
                      <span class="text-danger">*</span>
                    </label>
                    <input 
                      type="text" 
                      v-model="name" 
                      class="form-control form-control-lg" 
                      id="name" 
                      placeholder="Dr. John Doe"
                      required
                      style="border-radius: 10px;">
                    <small class="text-muted">Enter the doctor's complete name with title</small>
                  </div>

                  <!-- Email Field -->
                  <div class="mb-4">
                    <label for="email" class="form-label fw-semibold">
                      <i class="bi bi-envelope me-1 text-success"></i> Email Address
                      <span class="text-danger">*</span>
                    </label>
                    <input 
                      type="email" 
                      v-model="email" 
                      class="form-control form-control-lg" 
                      id="email" 
                      placeholder="doctor@hospital.com"
                      required
                      style="border-radius: 10px;">
                    <small class="text-muted">Professional email for system access and communications</small>
                  </div>

                  <!-- Password Field -->
                  <div class="mb-4">
                    <label for="password" class="form-label fw-semibold">
                      <i class="bi bi-lock me-1 text-success"></i> Password
                      <span class="text-danger">*</span>
                    </label>
                    <div class="position-relative">
                      <input 
                        :type="showPassword ? 'text' : 'password'" 
                        v-model="password" 
                        class="form-control form-control-lg" 
                        id="password" 
                        placeholder="Enter secure password"
                        required
                        style="border-radius: 10px; padding-right: 45px;">
                      <button 
                        type="button" 
                        class="btn position-absolute end-0 top-50 translate-middle-y"
                        @click="showPassword = !showPassword"
                        style="border: none; background: transparent;">
                        <i class="bi" :class="showPassword ? 'bi-eye-slash' : 'bi-eye'"></i>
                      </button>
                    </div>
                    <small class="text-muted">Minimum 8 characters with letters and numbers recommended</small>
                  </div>

                  <!-- Department Field -->
                  <div class="mb-4">
                    <label for="department" class="form-label fw-semibold">
                      <i class="bi bi-building me-1 text-success"></i> Department
                      <span class="text-danger">*</span>
                    </label>
                    <select 
                      v-model="department_id" 
                      class="form-select form-select-lg" 
                      id="department" 
                      required
                      style="border-radius: 10px;">
                      <option value="" disabled>Select a department</option>
                      <option v-for="d in departments" :key="d.id" :value="d.id">
                        {{ d.name }}
                      </option>
                    </select>
                    <small class="text-muted">Assign the doctor to their primary department</small>
                  </div>

                  <!-- Alert Messages -->
                  <div v-if="errorMessage" class="alert alert-danger d-flex align-items-center" role="alert" style="border-radius: 10px;">
                    <i class="bi bi-exclamation-triangle-fill me-2"></i>
                    <div>{{ errorMessage }}</div>
                  </div>

                  <div v-if="successMessage" class="alert alert-success d-flex align-items-center" role="alert" style="border-radius: 10px;">
                    <i class="bi bi-check-circle-fill me-2"></i>
                    <div>{{ successMessage }}</div>
                  </div>

                  <!-- Action Buttons -->
                  <div class="d-flex gap-3 mt-4">
                    <button 
                      type="submit" 
                      class="btn btn-success btn-lg flex-grow-1 d-flex align-items-center justify-content-center gap-2"
                      style="border-radius: 10px;">
                      <i class="bi bi-person-check"></i>
                      Register Doctor
                    </button>
                    <router-link 
                      to="/admin-dashboard" 
                      class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center gap-2"
                      style="border-radius: 10px; min-width: 120px;">
                      <i class="bi bi-x-circle"></i>
                      Cancel
                    </router-link>
                  </div>
                </form>
              </div>
            </div>

            <!-- Info Cards Row -->
            <div class="row g-3 mt-4">
              <!-- Security Info -->
              <div class="col-md-6">
                <div class="card border-0 bg-light h-100">
                  <div class="card-body">
                    <div class="d-flex">
                      <i class="bi bi-shield-check text-success me-3 fs-4"></i>
                      <div>
                        <h6 class="fw-bold mb-2">Security</h6>
                        <p class="mb-0 text-muted small">
                          Passwords are encrypted and secure. Doctors will be able to change their password after first login.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Access Info -->
              <div class="col-md-6">
                <div class="card border-0 bg-light h-100">
                  <div class="card-body">
                    <div class="d-flex">
                      <i class="bi bi-key text-primary me-3 fs-4"></i>
                      <div>
                        <h6 class="fw-bold mb-2">Access Rights</h6>
                        <p class="mb-0 text-muted small">
                          Registered doctors can view patients, manage appointments, and update medical records.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Tips Card -->
            <div class="card border-0 bg-light mt-3">
              <div class="card-body">
                <div class="d-flex">
                  <i class="bi bi-info-circle text-success me-3 fs-4"></i>
                  <div>
                    <h6 class="fw-bold mb-2">Registration Guidelines</h6>
                    <ul class="mb-0 text-muted small">
                      <li>Verify doctor credentials before registration</li>
                      <li>Use professional email addresses for all medical staff</li>
                      <li>Ensure accurate department assignment for proper workflow</li>
                      <li>Doctors will receive login credentials via email (if configured)</li>
                    </ul>
                  </div>
                </div>
              </div>
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
  color: white !important;
}

.sidebar {
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.card {
  transition: transform 0.2s, box-shadow 0.2s;
}

.form-control:focus,
.form-select:focus {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.15);
}

.btn {
  transition: all 0.2s;
  font-weight: 500;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.alert {
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.position-relative .btn {
  box-shadow: none !important;
}

.position-relative .btn:hover {
  transform: none;
  background-color: transparent !important;
}
</style>

<script>
export default {
    name: 'DoctorRegister',
    data() {
        return {
            name: '',
            email: '',
            password: '',
            department_id: '',
            departments: [],
            errorMessage: null,
            successMessage: null,
            showPassword: false
        }
    },
    methods: {
        async registerDoctor() {
            this.errorMessage = null;
            this.successMessage = null;
            const payload = {
                name: this.name,
                email: this.email,
                password: this.password,
                department_id: this.department_id,
                role: 'doctor'
            };
            try {
                const response = await fetch('/api/doctor', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
                    },
                    body: JSON.stringify(payload)
                });
                const result = await response.json();

                if (!response.ok) {
                    this.errorMessage = result.message;
                } else {
                    this.successMessage = result.message;
                    alert(result.message);
                    this.$router.push('/admin-dashboard');
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        },
        async fetchDepartment(){
            try {
                const response = await fetch('/api/department', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
                    }
                });
                const result = await response.json();
                if (!response.ok) {
                    this.errorMessage = result.message;
                } else {
                    this.departments = result;
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        }
    },
    mounted() {
        this.fetchDepartment();
    }
}
</script>
