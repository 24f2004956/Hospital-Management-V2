<template>
  <div v-if="show" class="modal fade show d-block" style="background: rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-lg">
      <div class="modal-content p-3">

        <h4 class="mb-3 text-center">Update Patient History</h4>

        <label>Diagnosis</label>
        <input v-model="form.diagnosis" class="form-control" />

        <label>Prescription</label>
        <input v-model="form.prescription" class="form-control" />

        <label>Notes</label>
        <textarea v-model="form.notes" class="form-control"></textarea>

        <label>Visit Type</label>
        <input v-model="form.visit_type" class="form-control" />

        <label>Test Done</label>
        <input v-model="form.test_done" class="form-control" />

        <label>Medicines</label>
        <textarea v-model="form.medicines" class="form-control"></textarea>

        <div class="mt-3 d-flex justify-content-end gap-2">
          <button class="btn btn-secondary" @click="close">Cancel</button>
          <button class="btn btn-primary" @click="save">Save</button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UpdatePatientHistory",
  props: ["show", "appointmentId"],
  data() {
    return {
      form: {
        diagnosis: "",
        prescription: "",
        notes: "",
        visit_type: "",
        test_done: "",
        medicines: ""
      }
    };
  },
  methods: {
    close() {
      this.$emit("close");
    },
    async save() {
      const response = await fetch(`/api/treatment/${this.appointmentId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem("doctorToken")}`
        },
        body: JSON.stringify(this.form)
      });

      const result = await response.json();
      if (!response.ok) {
        alert(result.message);
      } else {
        alert(" Patient History Updated Successfully!");
        this.close();
      }
    }
  }
};
</script>

<style>
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.5);
}
.modal-box {
  width: 420px;
  background: white;
  padding: 20px;
  border-radius: 8px;
  margin: 100px auto;
}
</style>
