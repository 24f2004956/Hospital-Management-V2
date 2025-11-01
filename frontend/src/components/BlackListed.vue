<template>
  <div class="container mt-5">

    <!-- Blacklisted Doctors -->
    <h3 class="mb-4 text-center">Blacklisted Doctors</h3>

    <table class="table table-bordered table-hover table-striped text-center">
      <thead class="table-dark">
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Email</th>
          <th>Contact</th>
          <th>Department</th>
          <th>Experience (Years)</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(doctor, index) in blacklistedDoctors" :key="doctor.id">
          <td>{{ index + 1 }}</td>
          <td>{{ doctor.name }}</td>
          <td>{{ doctor.email }}</td>
          <td>{{ doctor.contact || 'N/A' }}</td>
          <td>{{ doctor.department_name }}</td>
          <td>{{ doctor.experience_years || 'N/A' }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="unblacklistDoctor(doctor)">
              Unblacklist
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="blacklistedDoctors.length === 0" class="text-center text-muted">
      No blacklisted doctors found.
    </div>

    <hr class="my-5">

    <!-- Blacklisted Patients -->
    <h3 class="mb-4 text-center">Blacklisted Patients</h3>

    <table class="table table-bordered table-hover table-striped text-center">
      <thead class="table-dark">
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Email</th>
          <th>Age</th>
          <th>Gender</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(patient, index) in blacklistedPatients" :key="patient.id">
          <td>{{ index + 1 }}</td>
          <td>{{ patient.name }}</td>
          <td>{{ patient.email }}</td>
          <td>{{ patient.age || 'N/A' }}</td>
          <td>{{ patient.gender || 'N/A' }}</td>
          <td>
            <button class="btn btn-warning btn-sm" @click="unblacklistPatient(patient)">
              Unblacklist
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="blacklistedPatients.length === 0" class="text-center text-muted">
      No blacklisted patients found.
    </div>

  </div>
</template>

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
