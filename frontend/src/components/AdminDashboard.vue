<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm px-3">
    <a class="navbar-brand fw-bold" href="#">Admin Dashboard</a>

    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarContent">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item"><router-link to="/" class="nav-link">Home</router-link></li>
        <li class="nav-item"><router-link to="/create-department" class="nav-link">Create Department</router-link></li>
        <li class="nav-item"><router-link to="/doctor-register" class="nav-link">Doctor Registration</router-link></li>
        <li class="nav-item"><router-link to="/blacklisted" class="nav-link">Blacklisted Records</router-link></li>
        <li class="nav-item"><a class="nav-link" href="#patient-section">Patients</a></li>
        <li class="nav-item"><a class="nav-link" href="#doctor-section">Doctors</a></li>
        <li class="nav-item"><a class="nav-link" href="#department-section">Departments</a></li>
        <li class="nav-item"><button class="nav-link text-danger" @click="logout">Logout</button></li>
      </ul>

      <input v-model="globalSearch" class="form-control form-control-lg w-50"
        placeholder="Search Doctors, Patients, Departments, Appointments...">
    </div>
  </nav>

  <div v-if="!noResults" class="text-center text-muted mt-5">


    <div v-if="filteredDepartments.length" class="container mt-5">
      <h3 class="mb-4 text-center" id="department-section">Department List</h3>

      <table class="table table-bordered table-striped text-center shadow-sm">
        <thead class="table-dark">
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Description</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(department, index) in filteredDepartments" :key="department.id">
            <td>{{ index + 1 }}</td>
            <td>{{ department.name }}</td>
            <td>{{ department.description }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="openEditDepartment(department)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="deleteDepartment(department.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else-if="!isSearching" class="text-center text-muted mt-5">
      <h5>No departments available at the moment.</h5>
    </div>

    <div v-if="filteredDoctors.length" class="container mt-5">
      <h3 class="mb-4 text-center" id="doctor-section">Doctor List</h3>

      <table class="table table-bordered table-striped text-center shadow-sm">
        <thead class="table-dark">
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Email</th>
            <th>Contact</th>
            <th>Department</th>
            <th>Experience</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(doctor, index) in filteredDoctors" :key="doctor.id">
            <td>{{ index + 1 }}</td>
            <td>{{ doctor.name }}</td>
            <td>{{ doctor.email }}</td>
            <td>{{ doctor.contact || 'N/A' }}</td>
            <td>{{ doctor.department_name }}</td>
            <td>{{ doctor.experience_years || 'N/A' }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="openEditDoctor(doctor)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="deleteDoctor(doctor.id)">Delete</button>
              <button class="btn btn-dark btn-sm" @click="toggleBlacklistDoctor(doctor)">
                {{ doctor.black_list_status === 'active' ? 'Unblacklist' : 'Blacklist' }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else-if="!isSearching" class="text-center text-muted mt-5">
      <h5>No doctors available at the moment.</h5>
    </div>

    <div v-if="filteredPatients.length" class="container mt-5">
      <h3 class="mb-4 text-center" id="patient-section">Patient List</h3>

      <table class="table table-bordered table-striped text-center shadow-sm">
        <thead class="table-dark">
          <tr>
            <th>#</th>
            <th>Name</th>
            <th>Email</th>
            <th>Age</th>
            <th>Gender</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(patient, index) in filteredPatients" :key="patient.id">
            <td>{{ index + 1 }}</td>
            <td>{{ patient.name }}</td>
            <td>{{ patient.email }}</td>
            <td>{{ patient.age || 'N/A' }}</td>
            <td>{{ patient.gender || 'N/A' }}</td>
            <td>
              <button class="btn btn-warning btn-sm" @click="openEditPatient(patient)">Edit</button>
              <button class="btn btn-danger btn-sm" @click="deletePatient(patient.id)">Delete</button>
              <button class="btn btn-dark btn-sm" @click="toggleBlacklistPatient(patient)">
                {{ patient.black_list_status === 'active' ? 'Unblacklist' : 'Blacklist' }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else-if="!isSearching" class="text-center text-muted mt-5">
      <h5>No patients available at the moment.</h5>
    </div>

    <div v-if="filteredAppointments.length" class="container mt-5">
      <h3 class="mb-4 text-center">Upcoming Appointments</h3>

      <table class="table table-bordered table-striped text-center shadow-sm">
        <thead class="table-dark">
          <tr>
            <th>#</th>
            <th>Patient</th>
            <th>Doctor</th>
            <th>Department</th>
            <th>History</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(appointment, index) in filteredAppointments" :key="appointment.id">
            <td>{{ index + 1 }}</td>
            <td>{{ appointment.patient_name }}</td>
            <td>{{ appointment.doctor_name }}</td>
            <td>{{ appointment.department_name }}</td>
            <td>
              <button class="btn btn-info btn-sm" @click="openPatientHistory(appointment)">View</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else-if="!isSearching" class="text-center text-muted mt-5">
      <h5>No upcoming appointments scheduled.</h5>
    </div>
  </div>

  <div v-else class="text-center text-muted mt-5">
    <h5>No matching records found</h5>
  </div>


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
export default {
  name: 'AdminDashboard',
  components: { EditDoctor, EditDepartment, EditPatient, PatientHistory },
  data() {
    return {
      globalSearch: "",
      doctors: [],
      patients: [],
      departments: [],
      appointments: [],
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
