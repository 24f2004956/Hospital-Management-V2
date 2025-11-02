<template>
  <div class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-xl">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title">
            Patient History - {{ patient?.name || appointment?.patient_name }}
          </h5>
          <button class="btn-close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">
          <hr>
          <table class="table table-bordered text-center">
            <thead class="table-dark">
              <tr>
                <th>Visit No</th>
                <th>Doctor</th>
                <th>Department</th>
                <th>Diagnosis</th>
                <th>Prescription</th>
                <th>Medicines</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="(item, index) in filteredHistory" :key="item.id">
                <td>{{ index + 1 }}</td>
                <td>{{ item.doctor_name }}</td>
                <td>{{ item.department_name }}</td>
                <td>{{ item.diagnosis }}</td>
                <td>{{ item.prescription }}</td>
                <td>{{ item.medicines || 'N/A' }}</td>
              </tr>
            </tbody>
          </table>

          <div v-if="filteredHistory.length === 0" class="text-center text-muted">
            No history found for this patient.
          </div>

        </div>

        <div class="modal-footer">
          <button class="btn btn-secondary" @click="$emit('close')">Close</button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["appointment", "patient"],
  data() {
    return {
      history: [],
    };
  },
  computed: {
    filteredHistory() {
      // Determine patient ID
      const patientId = this.patient?.id || this.appointment?.patient_id;

      if (!patientId) return [];

      // Filter all history of that one patient
      return this.history.filter(item => item.patient_id === patientId);
    }
  },
  async mounted() {
    let token = null;
    let url = null;

    if (localStorage.getItem('adminToken')) {
      token = localStorage.getItem('adminToken');
      url = '/api/treatment/admin';
    }
    else if (localStorage.getItem('doctorToken')) {
      token = localStorage.getItem('doctorToken');
      url = '/api/treatment/doctor';
    }
    else if (localStorage.getItem('patientToken')) {
      token = localStorage.getItem('patientToken');
      url = '/api/treatment/patient';
    }
    else {
      return;
    }

    const response = await fetch(url, {
      headers: {
        "Authorization": `Bearer ${token}`
      }
    });

    this.history = await response.json();
  }
};  
</script>

<style scoped>
.modal-body {
  max-height: 70vh;
  overflow-y: auto;
}
</style>
