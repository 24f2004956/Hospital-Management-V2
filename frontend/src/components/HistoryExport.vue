<template>
  <div class="container mt-4">
    <div class="header-row">
      <h2 class="text-center mb-4">
        My Medical History
        <span v-if="patient.name"> - {{ patient.name }}</span>
      </h2>
      <button class="export-btn" @click="exportCSV">Export as CSV</button>
    </div>

    <hr>
    <table class="table table-bordered table-hover text-center align-middle">
        
      <thead class="table-dark">
        <tr>
          <th>#</th>
          <th>Doctor</th>
          <th>Department</th>
          <th>Diagnosis</th>
          <th>Prescription</th>
          <th>Medicines</th>
          <th>Date</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(item, index) in history" :key="item.id">
          <td>{{ index + 1 }}</td>
          <td>{{ item.doctor_name }}</td>
          <td>{{ item.department_name }}</td>
          <td>{{ item.diagnosis }}</td>
          <td>{{ item.prescription }}</td>
          <td>{{ item.medicines || 'N/A' }}</td>
          <td>{{ formatDate(item.date) }}</td>
        </tr>
      </tbody>
    </table>

    <div v-if="history.length === 0" class="text-center text-muted fw-bold mt-3">
      No medical history available.
    </div>

    <div class="text-center mt-4">
      <router-link to="/patient-dashboard" class="btn btn-secondary">
        ← Back to Dashboard
      </router-link>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      patient: {},
      history: [],
      message: "",
    };
  },

  async mounted() {
    const token = localStorage.getItem("patientToken");
    if (!token) return;

    // Fetch patient profile
    const profileResp = await fetch("/api/patient", {
      headers: { "Authorization": `Bearer ${token}` }
    });
    this.patient = await profileResp.json();

    // Fetch patient treatment history
    const historyResp = await fetch("/api/treatment/patient", {
      headers: { "Authorization": `Bearer ${token}` }
    });
    this.history = await historyResp.json();
  },

  methods: {
    formatDate(dateString) {
      if (!dateString) return "N/A";
      const date = new Date(dateString);
      return date.toISOString().slice(0, 10);
    },
    async exportCSV(){
        const token = localStorage.getItem("patientToken");
        if (!token) return;
    
        const response = await fetch("/api/treatment/export", {
            headers: { "Authorization": `Bearer ${token}` }
        });
        const result = await response.json();
    
        if (!response.ok) {
            alert("request failed");
            return;
        }else{
            alert(result.message);
        }
    }
  }
};
</script>

<style scoped>
.table {
  font-size: 15px;
}
.table thead {
  font-size: 16px;
}
.header-row {
  display: flex;
  justify-content: space-between; /* pushes button to right */
  align-items: center;
  margin-bottom: 15px;
}

</style>
