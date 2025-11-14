<template>
  <!-- Modern Sidebar Navigation -->
  <div class="d-flex min-vh-100">
    <!-- Sidebar -->
    <nav class="sidebar bg-dark text-white d-flex flex-column p-3"
      style="width: 260px; position: fixed; height: 100vh; overflow-y: auto;">
      <div class="mb-4">
        <h4 class="fw-bold text-white mb-0">
          <i class="bi bi-hospital"></i> Admin Portal
        </h4>
        <small class="text-white-50">Healthcare Management</small>
      </div>

      <ul class="nav flex-column gap-2">
        <li class="nav-item">
          <router-link to="/admin-dashboard"
            class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight">
            <i class="bi bi-speedometer2 me-2"></i> Dashboard
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/create-department" class="nav-link text-white rounded d-flex align-items-center py-2 px-3"
            style="background: rgba(255,255,255,0.1);">
            <i class="bi bi-building me-2"></i> Create Department
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/doctor-register"
            class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight">
            <i class="bi bi-person-plus me-2"></i> Register Doctor
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/blacklisted"
            class="nav-link text-white-50 rounded d-flex align-items-center py-2 px-3 hover-highlight">
            <i class="bi bi-shield-x me-2"></i> Blacklisted Records
          </router-link>
        </li>

        <hr class="border-white-50 my-3">


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
            <h5 class="mb-0 fw-bold text-dark">Create New Department</h5>
            <small class="text-muted">Add a new department to your healthcare system</small>
          </div>
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mb-0">
              <li class="breadcrumb-item">
                <router-link to="/admin-dashboard" class="text-decoration-none">Dashboard</router-link>
              </li>
              <li class="breadcrumb-item active">Create Department</li>
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
                  <div
                    class="bg-primary bg-opacity-10 rounded-circle d-flex align-items-center justify-content-center me-3"
                    style="width: 50px; height: 50px;">
                    <i class="bi bi-building text-primary fs-4"></i>
                  </div>
                  <div>
                    <h5 class="mb-0 fw-bold">Department Information</h5>
                    <small class="text-muted">Fill in the details below</small>
                  </div>
                </div>

                <form @submit.prevent="createDepartment">
                  <!-- Name Field -->
                  <div class="mb-4">
                    <label for="name" class="form-label fw-semibold">
                      <i class="bi bi-tag me-1 text-primary"></i> Department Name
                      <span class="text-danger">*</span>
                    </label>
                    <input type="text" v-model="name" class="form-control form-control-lg" id="name"
                      placeholder="e.g., Cardiology, Pediatrics, Emergency" required style="border-radius: 10px;">
                    <small class="text-muted">Enter a clear and descriptive name for the department</small>
                  </div>

                  <!-- Description Field -->
                  <div class="mb-4">
                    <label for="description" class="form-label fw-semibold">
                      <i class="bi bi-text-left me-1 text-primary"></i> Description
                      <span class="text-danger">*</span>
                    </label>
                    <textarea v-model="description" class="form-control form-control-lg" id="description" rows="5"
                      placeholder="Provide a detailed description of the department's services and specialties..."
                      required style="border-radius: 10px;"></textarea>
                    <small class="text-muted">Describe the department's purpose and services offered</small>
                  </div>

                  <!-- Alert Messages -->
                  <div v-if="errorMessage" class="alert alert-danger d-flex align-items-center" role="alert"
                    style="border-radius: 10px;">
                    <i class="bi bi-exclamation-triangle-fill me-2"></i>
                    <div>{{ errorMessage }}</div>
                  </div>

                  <div v-if="successMessage" class="alert alert-success d-flex align-items-center" role="alert"
                    style="border-radius: 10px;">
                    <i class="bi bi-check-circle-fill me-2"></i>
                    <div>{{ successMessage }}</div>
                  </div>

                  <!-- Action Buttons -->
                  <div class="d-flex gap-3 mt-4">
                    <button type="submit"
                      class="btn btn-primary btn-lg flex-grow-1 d-flex align-items-center justify-content-center gap-2"
                      style="border-radius: 10px;">
                      <i class="bi bi-plus-circle"></i>
                      Create Department
                    </button>
                    <router-link to="/admin-dashboard"
                      class="btn btn-outline-secondary btn-lg d-flex align-items-center justify-content-center gap-2"
                      style="border-radius: 10px; min-width: 120px;">
                      <i class="bi bi-x-circle"></i>
                      Cancel
                    </router-link>
                  </div>
                </form>
              </div>
            </div>

            <!-- Info Card -->
            <div class="card border-0 bg-light mt-4">
              <div class="card-body">
                <div class="d-flex">
                  <i class="bi bi-info-circle text-primary me-3 fs-4"></i>
                  <div>
                    <h6 class="fw-bold mb-2">Tips for Creating Departments</h6>
                    <ul class="mb-0 text-muted small">
                      <li>Use clear, standardized names for easy identification</li>
                      <li>Provide comprehensive descriptions to help patients understand services</li>
                      <li>Ensure department names are unique within your system</li>
                      <li>Include information about specialized equipment or treatments if applicable</li>
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



<script>
export default {
  name: 'CreateDepartment',
  data() {
    return {
      name: '',
      description: '',
      errorMessage: null,
      successMessage: null,
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('adminToken');
      this.$router.push('/');
    },
    async createDepartment() {
      this.errorMessage = null;
      this.successMessage = null;
      const payload = {
        name: this.name,
        description: this.description
      };
      try {
        const response = await fetch('/api/department', {
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

  },
}
</script>

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

.form-control:focus {
  border-color: #0d6efd;
  box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.15);
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
</style>
