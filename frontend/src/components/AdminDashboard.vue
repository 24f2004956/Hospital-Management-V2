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

      <div class="mb-4 p-3 bg-white bg-opacity-10 rounded">
        <div class="d-flex align-items-center">
          <div class="bg-primary rounded-circle d-flex align-items-center justify-content-center me-2" 
               style="width: 40px; height: 40px;">
            <i class="bi bi-person-fill text-white"></i>
          </div>
          <div>
            <div class="fw-semibold">{{ username }}</div>
            <small class="text-white-50">Administrator</small>
          </div>
        </div>
      </div>

      <ul class="nav flex-column gap-2">
        <li class="nav-item">
          <a class="nav-link text-white rounded d-flex align-items-center py-2 px-3" href="#" 
             style="background: rgba(255,255,255,0.1);">
            <i class="bi bi-speedometer2 me-2"></i> Dashboard
          </a>
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
      <header class="bg-white shadow-sm sticky-top p-3 mb-4">
        <div class="d-flex justify-content-between align-items-center">
          <div>
            <h5 class="mb-0 fw-bold text-dark">Dashboard Overview</h5>
            <small class="text-muted">Welcome back, manage your healthcare system</small>
          </div>
          <div class="d-flex gap-3 align-items-center">
            <div class="position-relative" style="max-width: 400px;">
              <i class="bi bi-search position-absolute" style="left: 12px; top: 50%; transform: translateY(-50%); color: #6c757d;"></i>
              <input v-model="globalSearch" 
                     class="form-control ps-5" 
                     style="border-radius: 20px; border: 1px solid #dee2e6;"
                     placeholder="Search anything...">
            </div>
            <button @click="downloadPDF" class="btn btn-primary d-flex align-items-center gap-2" 
                    style="border-radius: 20px;">
              <i class="bi bi-download"></i> Export PDF
            </button>
          </div>
        </div>
      </header>

      <!-- Content Container -->
      <div class="container-fluid px-4 pb-4">
        <!-- Data Tables -->
        <div v-if="!noResults">
          <!-- Charts Section -->
        <div class="row g-4 mb-4" v-if="appointmentsTrend.length || departmentDemandData.length">
          <div class="col-lg-6" v-if="appointmentsTrend.length">
            <div class="card border-0 shadow-sm h-100">
              <div class="card-body">
                <h6 class="card-title fw-bold mb-3">
                  <i class="bi bi-graph-up text-primary me-2"></i>Appointments Trend
                </h6>
                <AppointmentsChart :chartData="appointmentsTrend" />
              </div>
            </div>
          </div>
          <div class="col-lg-6" v-if="departmentDemandData.length">
            <div class="card border-0 shadow-sm h-100">
              <div class="card-body">
                <h6 class="card-title fw-bold mb-3">
                  <i class="bi bi-bar-chart text-success me-2"></i>Department Demand
                </h6>
                <DepartmentDemandChart :chartData="departmentDemandData" />
              </div>
            </div>
          </div>
        </div>
          <!-- Departments Table -->
          <div v-if="filteredDepartments.length" class="card border-0 shadow-sm mb-4" id="department-section">
            <div class="card-header bg-white border-0 py-3">
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="mb-0 fw-bold">
                  <i class="bi bi-diagram-3 text-primary me-2"></i>Departments
                </h5>
                <span class="badge bg-primary rounded-pill">{{ filteredDepartments.length }}</span>
              </div>
            </div>
            <div class="card-body p-0">
              <div class="table-responsive">
                <table class="table table-hover mb-0">
                  <thead style="background: #f8f9fa;">
                    <tr>
                      <th class="text-muted fw-semibold py-3" style="width: 60px;">#</th>
                      <th class="text-muted fw-semibold py-3">Name</th>
                      <th class="text-muted fw-semibold py-3">Description</th>
                      <th class="text-muted fw-semibold py-3 text-end" style="width: 200px;">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(department, index) in filteredDepartments" :key="department.id">
                      <td class="py-3 text-muted">{{ index + 1 }}</td>
                      <td class="py-3 fw-semibold">{{ department.name }}</td>
                      <td class="py-3 text-muted">{{ department.description }}</td>
                      <td class="py-3 text-end">
                        <button class="btn btn-sm btn-outline-primary me-2" @click="openEditDepartment(department)">
                          <i class="bi bi-pencil"></i>
                        </button>
                        <button class="btn btn-sm btn-outline-danger" @click="deleteDepartment(department.id)">
                          <i class="bi bi-trash"></i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div v-else-if="!isSearching" class="card border-0 shadow-sm mb-4">
            <div class="card-body text-center py-5">
              <i class="bi bi-diagram-3 text-muted" style="font-size: 3rem;"></i>
              <h5 class="text-muted mt-3">No departments available</h5>
              <p class="text-muted">Create your first department to get started</p>
            </div>
          </div>

          <!-- Doctors Table -->
          <div v-if="filteredDoctors.length" class="card border-0 shadow-sm mb-4" id="doctor-section">
            <div class="card-header bg-white border-0 py-3">
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="mb-0 fw-bold">
                  <i class="bi bi-person-badge text-success me-2"></i>Doctors
                </h5>
                <span class="badge bg-success rounded-pill">{{ filteredDoctors.length }}</span>
              </div>
            </div>
            <div class="card-body p-0">
              <div class="table-responsive">
                <table class="table table-hover mb-0">
                  <thead style="background: #f8f9fa;">
                    <tr>
                      <th class="text-muted fw-semibold py-3" style="width: 60px;">#</th>
                      <th class="text-muted fw-semibold py-3">Name</th>
                      <th class="text-muted fw-semibold py-3">Email</th>
                      <th class="text-muted fw-semibold py-3">Contact</th>
                      <th class="text-muted fw-semibold py-3">Department</th>
                      <th class="text-muted fw-semibold py-3">Experience</th>
                      <th class="text-muted fw-semibold py-3 text-end" style="width: 240px;">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(doctor, index) in filteredDoctors" :key="doctor.id">
                      <td class="py-3 text-muted">{{ index + 1 }}</td>
                      <td class="py-3">
                        <div class="fw-semibold">{{ doctor.name }}</div>
                      </td>
                      <td class="py-3 text-muted">{{ doctor.email }}</td>
                      <td class="py-3 text-muted">{{ doctor.contact || 'N/A' }}</td>
                      <td class="py-3">
                        <span class="badge bg-light text-dark">{{ doctor.department_name }}</span>
                      </td>
                      <td class="py-3 text-muted">{{ doctor.experience_years || 'N/A' }} yrs</td>
                      <td class="py-3 text-end">
                        <button class="btn btn-sm btn-outline-primary me-1" @click="openEditDoctor(doctor)">
                          <i class="bi bi-pencil"></i>
                        </button>
                        <button class="btn btn-sm btn-outline-danger me-1" @click="deleteDoctor(doctor.id)">
                          <i class="bi bi-trash"></i>
                        </button>
                        <button class="btn btn-sm" 
                                :class="doctor.black_list_status === 'active' ? 'btn-outline-warning' : 'btn-outline-dark'"
                                @click="toggleBlacklistDoctor(doctor)">
                          <i class="bi" :class="doctor.black_list_status === 'active' ? 'bi-shield-check' : 'bi-shield-x'"></i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div v-else-if="!isSearching" class="card border-0 shadow-sm mb-4">
            <div class="card-body text-center py-5">
              <i class="bi bi-person-badge text-muted" style="font-size: 3rem;"></i>
              <h5 class="text-muted mt-3">No doctors registered</h5>
              <p class="text-muted">Register doctors to manage appointments</p>
            </div>
          </div>

          <!-- Patients Table -->
          <div v-if="filteredPatients.length" class="card border-0 shadow-sm mb-4" id="patient-section">
            <div class="card-header bg-white border-0 py-3">
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="mb-0 fw-bold">
                  <i class="bi bi-people text-info me-2"></i>Patients
                </h5>
                <span class="badge bg-info rounded-pill">{{ filteredPatients.length }}</span>
              </div>
            </div>
            <div class="card-body p-0">
              <div class="table-responsive">
                <table class="table table-hover mb-0">
                  <thead style="background: #f8f9fa;">
                    <tr>
                      <th class="text-muted fw-semibold py-3" style="width: 60px;">#</th>
                      <th class="text-muted fw-semibold py-3">Name</th>
                      <th class="text-muted fw-semibold py-3">Email</th>
                      <th class="text-muted fw-semibold py-3">Age</th>
                      <th class="text-muted fw-semibold py-3">Gender</th>
                      <th class="text-muted fw-semibold py-3 text-end" style="width: 240px;">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(patient, index) in filteredPatients" :key="patient.id">
                      <td class="py-3 text-muted">{{ index + 1 }}</td>
                      <td class="py-3 fw-semibold">{{ patient.name }}</td>
                      <td class="py-3 text-muted">{{ patient.email }}</td>
                      <td class="py-3 text-muted">{{ patient.age || 'N/A' }}</td>
                      <td class="py-3">
                        <span class="badge" :class="patient.gender === 'Male' ? 'bg-primary' : 'bg-danger'">
                          {{ patient.gender || 'N/A' }}
                        </span>
                      </td>
                      <td class="py-3 text-end">
                        <button class="btn btn-sm btn-outline-primary me-1" @click="openEditPatient(patient)">
                          <i class="bi bi-pencil"></i>
                        </button>
                        <button class="btn btn-sm btn-outline-danger me-1" @click="deletePatient(patient.id)">
                          <i class="bi bi-trash"></i>
                        </button>
                        <button class="btn btn-sm" 
                                :class="patient.black_list_status === 'active' ? 'btn-outline-warning' : 'btn-outline-dark'"
                                @click="toggleBlacklistPatient(patient)">
                          <i class="bi" :class="patient.black_list_status === 'active' ? 'bi-shield-check' : 'bi-shield-x'"></i>
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div v-else-if="!isSearching" class="card border-0 shadow-sm mb-4">
            <div class="card-body text-center py-5">
              <i class="bi bi-people text-muted" style="font-size: 3rem;"></i>
              <h5 class="text-muted mt-3">No patients registered</h5>
              <p class="text-muted">Patient records will appear here</p>
            </div>
          </div>

          <!-- Appointments Table -->
          <div v-if="filteredAppointments.length" class="card border-0 shadow-sm mb-4">
            <div class="card-header bg-white border-0 py-3">
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="mb-0 fw-bold">
                  <i class="bi bi-calendar-check text-warning me-2"></i>Upcoming Appointments
                </h5>
                <span class="badge bg-warning text-dark rounded-pill">{{ filteredAppointments.length }}</span>
              </div>
            </div>
            <div class="card-body p-0">
              <div class="table-responsive">
                <table class="table table-hover mb-0">
                  <thead style="background: #f8f9fa;">
                    <tr>
                      <th class="text-muted fw-semibold py-3" style="width: 60px;">#</th>
                      <th class="text-muted fw-semibold py-3">Patient</th>
                      <th class="text-muted fw-semibold py-3">Doctor</th>
                      <th class="text-muted fw-semibold py-3">Department</th>
                      <th class="text-muted fw-semibold py-3 text-end" style="width: 120px;">History</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(appointment, index) in filteredAppointments" :key="appointment.id">
                      <td class="py-3 text-muted">{{ index + 1 }}</td>
                      <td class="py-3 fw-semibold">{{ appointment.patient_name }}</td>
                      <td class="py-3">{{ appointment.doctor_name }}</td>
                      <td class="py-3">
                        <span class="badge bg-light text-dark">{{ appointment.department_name }}</span>
                      </td>
                      <td class="py-3 text-end">
                        <button class="btn btn-sm btn-outline-info" @click="openPatientHistory(appointment)">
                          <i class="bi bi-eye me-1"></i> View
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div v-else-if="!isSearching" class="card border-0 shadow-sm mb-4">
            <div class="card-body text-center py-5">
              <i class="bi bi-calendar-x text-muted" style="font-size: 3rem;"></i>
              <h5 class="text-muted mt-3">No upcoming appointments</h5>
              <p class="text-muted">Scheduled appointments will appear here</p>
            </div>
          </div>
        </div>

        <!-- No Results -->
        <div v-else class="card border-0 shadow-sm">
          <div class="card-body text-center py-5">
            <i class="bi bi-search text-muted" style="font-size: 3rem;"></i>
            <h5 class="text-muted mt-3">No matching records found</h5>
            <p class="text-muted">Try adjusting your search criteria</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modals -->
  <EditDoctor v-if="showEditDoctorModal" :doctor="selectedDoctor" :departments="departments"
    @close="showEditDoctorModal = false" @updated="showEditDoctorModal = false; fetchDoctors();" />

  <EditDepartment v-if="showEditDepartmentModal" :department="selectedDepartment"
    @close="showEditDepartmentModal = false" @updated="showEditDepartmentModal = false; fetchDepartments();" />

  <EditPatient v-if="showEditPatientModal" :patient="selectedPatient" @close="showEditPatientModal = false"
    @updated="showEditPatientModal = false; fetchPatients();" />

  <PatientHistory v-if="showPatientHistoryModal" :patient="selectedPatient" @close="showPatientHistoryModal = false" />
</template>

<script>
import EditDepartment from './EditDepartment.vue';
import EditDoctor from './EditDoctor.vue';
import EditPatient from './EditPatient.vue';
import PatientHistory from './PatientHistory.vue';
import AppointmentsChart from "./charts/AppointmentChart.vue";
import DepartmentDemandChart from "./charts/DepartmentDemand.vue";

export default {
  name: 'AdminDashboard',
  components: { EditDoctor, EditDepartment, EditPatient, PatientHistory, AppointmentsChart, DepartmentDemandChart },
  data() {
    return {
      username: localStorage.getItem("username") || "",
      globalSearch: "",
      doctors: [],
      patients: [],
      departments: [],
      departmentDemandData: [],
      appointments: [],
      appointmentsTrend: [],
      showPatientHistoryModal: false,
      selectedAppointment: null,
      showEditDoctorModal: false,
      showEditDepartmentModal: false,
      showEditPatientModal: false,
      selectedDoctor: null,
      selectedPatient: null,
      selectedDepartment: null,
      errorMessage: ""
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('adminToken');
      this.$router.push('/');
    },
    async fetchAppointmentTrend() {
      const res = await fetch("/api/report/appointments-trend", {
        headers: { Authorization: `Bearer ${localStorage.getItem("adminToken")}` }
      });
      this.appointmentsTrend = await res.json();
      console.log("CHART DATA RECEIVED:", this.appointmentsTrend);
    },

    async fetchDepartmentDemand() {
      const res = await fetch("/api/report/department-demand", {
        headers: { Authorization: `Bearer ${localStorage.getItem("adminToken")}` }
      });
      this.departmentDemandData = await res.json();
      console.log("DEPARTMENT DEMAND RECEIVED:", this.departmentDemandData);
    },

    async downloadPDF() {
            const month = "2025-11"; // You can use a date picker to make dynamic

            const response = await fetch(`/api/reports/monthly?month=${month}`, {
                method: 'GET',
                headers: {'Authorization': `Bearer ${localStorage.getItem('adminToken')}`}
            });

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `Monthly_Report_${month}.pdf`;
            a.click();
            window.URL.revokeObjectURL(url);
        },

    async fetchDoctors() {
      try {
        const response = await fetch('/api/doctor', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
          }
        });

        const result = await response.json();
        if (!response.ok) {
          this.errorMessage = result.message;
        } else {
          this.doctors = result;
        }
      } catch (error) {
        this.errorMessage = 'Unable to connect to the server. Please try again later.';
      }
    },
    async fetchPatients() {
      try {
        const response = await fetch('/api/patient', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
          }
        });

        const result = await response.json();
        if (!response.ok) {
          this.errorMessage = result.message;
        } else {
          this.patients = Array.isArray(result) ? result : [result];

        }
      } catch (error) {
        this.errorMessage = 'Unable to connect to the server. Please try again later.';
      }
    },
    async fetchDepartments() {
      try {
        const response = await fetch('/api/department', {
          method: 'GET',
          headers: {
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
    },

    async fetchAppointments() {
      try {
        const response = await fetch('/api/appointment', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
          }
        });
        const result = await response.json();
        if (!response.ok) {
          this.errorMessage = result.message;
        } else {
          this.appointments = result;
        }
      } catch (error) {
        this.errorMessage = 'Unable to connect to the server. Please try again later.';
      }
    },

    async deleteDoctor(id) {
      if (!confirm("Are you sure you want to delete this doctor?")) return;

      try {
        const response = await fetch(`/api/doctor/${id}`, {
          method: "DELETE",
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
          }
        });

        const result = await response.json();
        if (!response.ok) {
          alert(result.message);
        } else {
          alert("Doctor deleted successfully");
          this.fetchDoctors();
        }
      } catch (err) {
        alert("Server error!");
      }
    },

    async deleteDepartment(id) {
      if (!confirm("Are you sure you want to delete this department?")) return;

      try {
        const response = await fetch(`/api/department/${id}`, {
          method: "DELETE",
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
          }
        });

        const result = await response.json();
        if (!response.ok) {
          alert(result.message);
        } else {
          alert("Department deleted successfully");
          this.fetchDepartments();
        }
      } catch (err) {
        alert("Server error!");
      }
    },

    async deletePatient(id) {
      if (!confirm("Are you sure you want to delete this patient?")) return;

      try {
        const response = await fetch(`/api/patient/${id}`, {
          method: "DELETE",
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('adminToken')}`
          }
        });

        const result = await response.json();
        if (!response.ok) {
          alert(result.message);
        } else {
          alert("Patient deleted successfully");
          this.fetchPatients();
        }
      } catch (err) {
        alert("Server error!");
      }
    },

    async toggleBlacklistDoctor(doctor) {
      const newStatus = doctor.black_list_status === "active" ? "deactive" : "active";

      if (!confirm(`Are you sure you want to ${newStatus === 'active' ? 'blacklist' : 'remove blacklist'} this doctor?`)) return;

      try {
        const response = await fetch(`/api/account/doctor/${doctor.id}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('adminToken')}`
          },
          body: JSON.stringify({ status: newStatus })
        });

        const result = await response.json();

        if (!response.ok) {
          alert(result.message);
        } else {
          alert(result.message);
          this.fetchDoctors(); // Refresh list
        }

      } catch (err) {
        alert("Server Error");
      }
    },
    async toggleBlacklistPatient(patient) {
      const newStatus = patient.black_list_status === "active" ? "deactive" : "active";

      if (!confirm(`Are you sure you want to ${newStatus === 'active' ? 'blacklist' : 'remove blacklist'} this patient?`)) return;

      try {
        const response = await fetch(`/api/account/patient/${patient.id}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('adminToken')}`
          },
          body: JSON.stringify({ status: newStatus })
        });

        const result = await response.json();

        if (!response.ok) {
          alert(result.message);
        } else {
          alert(result.message);
          this.fetchPatients(); // Refresh list
        }

      } catch (err) {
        alert("Server Error");
      }
    },
    openEditDoctor(doctor) {
      this.selectedDoctor = { ...doctor };  // make a copy
      this.showEditDoctorModal = true;
    },

    openEditDepartment(department) {
      this.selectedDepartment = { ...department }; // make a copy
      this.showEditDepartmentModal = true;
    },

    openEditPatient(patient) {
      this.selectedPatient = { ...patient }; // make a copy
      this.showEditPatientModal = true;
    },
    openPatientHistory(appointment) {
      this.selectedPatient = {
        id: appointment.patient_id,
        name: appointment.patient_name
      };
      this.showPatientHistoryModal = true;
    }

  },
  mounted() {
    this.fetchDoctors();
    this.fetchPatients();
    this.fetchDepartments();
    this.fetchAppointments();
    this.fetchAppointmentTrend();
    this.fetchDepartmentDemand();
  },
  computed: {
    activeDoctors() {
      return this.doctors.filter(d => d.black_list_status === 'deactive');

    },
    activePatients() {
      return Array.isArray(this.patients)
        ? this.patients.filter(p => p.black_list_status === 'deactive')
        : [];
    }
    ,
    filteredDoctors() {
      const key = this.globalSearch.toLowerCase();
      return this.activeDoctors.filter(d =>
        d.name.toLowerCase().includes(key) ||
        (d.email && d.email.toLowerCase().includes(key)) ||
        (d.contact && d.contact.toLowerCase().includes(key)) ||
        (d.department_name && d.department_name.toLowerCase().includes(key)) ||
        d.id.toString().includes(key)
      );
    },

    filteredPatients() {
      const key = this.globalSearch.toLowerCase();
      return this.activePatients.filter(p =>
        p.name.toLowerCase().includes(key) ||
        (p.email && p.email.toLowerCase().includes(key)) ||
        (p.contact && p.contact.toLowerCase().includes(key)) ||
        p.id.toString().includes(key)
      );
    },

    filteredDepartments() {
      const key = this.globalSearch.toLowerCase();
      return this.departments.filter(dep =>
        dep.name.toLowerCase().includes(key) ||
        dep.description.toLowerCase().includes(key) ||
        dep.id.toString().includes(key)
      );
    },
    filteredAppointments() {
      if (!this.globalSearch) return this.appointments;

      const s = this.globalSearch.toLowerCase();

      return this.appointments.filter(a =>
        a.patient_name.toLowerCase().includes(s) ||
        a.doctor_name.toLowerCase().includes(s) ||
        a.department_name.toLowerCase().includes(s) ||
        a.reason.toLowerCase().includes(s)
      );
    },
    noResults() {
      return (
        this.globalSearch.trim() &&
        !this.filteredDoctors.length &&
        !this.filteredPatients.length &&
        !this.filteredDepartments.length &&
        !this.filteredAppointments.length
      );
    },
    isSearching() {
      return this.globalSearch.trim().length > 0;
    }

  }
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

.table-hover tbody tr:hover {
  background-color: #f8f9fa;
}

.card {
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
}

.btn {
  transition: all 0.2s;
}

.btn:hover {
  transform: translateY(-1px);
}
</style>

