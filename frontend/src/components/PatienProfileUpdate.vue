<template>
  <div class="container mt-4">
    <h2>Edit Profile</h2>

    <div v-if="patient" class="card p-4 shadow-sm">

      <div class="mb-3">
        <label class="form-label">Name</label>
        <input v-model="patient.name" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">Email</label>
        <input v-model="patient.email" class="form-control" />
      </div>

      <div class="mb-3">
        <label class="form-label">Gender</label>
        <select v-model="patient.gender" class="form-control">
          <option>Male</option>
          <option>Female</option>
          <option>Other</option>
        </select>
      </div>

      <div class="mb-3">
        <label class="form-label">Age (Years)</label>
        <input type="number" v-model="patient.age" class="form-control" />
      </div>

      <button class="btn btn-secondary me-2" @click="$router.back()">Back</button>
      <button class="btn btn-success" @click="updateProfile">Save Changes</button>

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
