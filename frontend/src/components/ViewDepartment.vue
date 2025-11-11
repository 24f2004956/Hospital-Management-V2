<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm px-3">
        <a class="navbar-brand fw-bold" href="#">Patient Dashboard</a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item"><router-link to="/" class="nav-link">Home</router-link></li>
                <li class="nav-item"><router-link to="/patient-profile-update" class="nav-link">Edit
                        Profile</router-link></li>
                <li class="nav-item"><router-link to="/history-export" class="nav-link">History</router-link></li>
                <li class="nav-item"><button class="nav-link text-danger" @click="logout">Logout</button></li>
            </ul>
        </div>
    </nav>
  <div class="container mt-4">
    <button class="btn btn-secondary mb-3" @click="$router.back()">← Back</button>

    <div v-if="loading" class="text-center"><h5>Loading...</h5></div>

    <div v-if="department">
      <h2 class="fw-bold">{{ department.name }}</h2>
      <p class="text-muted">{{ department.description }}</p>

      <h4 class="mt-4">Doctors in this Department</h4>

      <table class="table table-bordered table-hover mt-3 text-center">
        <thead class="table-dark">
          <tr>
            <th>#</th>
            <th>Doctor Name</th>
            <th>Experience</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(doctor, index) in doctors" :key="doctor.id">
            <td>{{ index + 1 }}</td>
            <td>{{ doctor.name }}</td>
            <td>{{ doctor.experience_years }} years</td>
            <td>
              <button class="btn btn-info btn-sm me-2" @click="viewDoctor(doctor)">View Profile</button>
              <button class="btn btn-primary btn-sm" @click="checkAvailability(doctor)">Check Availability</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else-if="!loading" class="text-center text-muted"><h5>No data found.</h5></div>

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
    }
  }
};
</script>

<style scoped>
h2 { color: #003366; }
</style>
