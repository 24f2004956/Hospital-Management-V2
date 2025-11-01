<template>
  <div class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-xl">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title">
            Patient History - {{ appointment.patient_name }}
          </h5>
          <button class="btn-close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">

          <p><strong>Doctor:</strong> {{ appointment.doctor_name }}</p>
          <p><strong>Department:</strong> {{ appointment.department_name }}</p>

          <hr>

          <table class="table table-bordered text-center">
            <thead class="table-dark">
              <tr>
                <th>Visit No</th>
                <th>Visit Type</th>
                <th>Test Done</th>
                <th>Diagnosis</th>
                <th>Prescription</th>
                <th>Medicines</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="(item, index) in filteredHistory" :key="item.id">
                <td>{{ index + 1 }}</td>
                <td>{{ item.visit_type || 'N/A' }}</td>
                <td>{{ item.test_done || 'N/A' }}</td>
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
  props: ["appointment"],
  data() {
    return {
      history: []
    };
  },
  computed: {
    filteredHistory() {
      return this.history.filter(item => item.appointment_id === this.appointment.id);
    }
  },
  async mounted() {
    const response = await fetch('/api/treatment/all', {
      headers: {
        "Authorization": `Bearer ${localStorage.getItem('adminToken')}`
      }
    });

    this.history = await response.json();
  }
}
</script>

<style scoped>
.modal-body {
  max-height: 70vh;
  overflow-y: auto;
}
</style>
