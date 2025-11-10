<template>
  <div class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-lg">
      <div class="modal-content" v-if="localPatient">

        <div class="modal-header">
          <h5 class="modal-title">Edit Patient</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">

          <div class="mb-3">
            <label class="form-label">Name</label>
            <input v-model="localPatient.name" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Email</label>
            <input v-model="localPatient.email" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Gender</label>
            <select v-model="localPatient.gender" class="form-control">
              <option value="Male">Male</option>
              <option value="Female">Female</option>
              <option value="Other">Other</option>
            </select>
          </div>

          <div class="mb-3">
            <label class="form-label">Age (Years)</label>
            <input type="number" v-model="localPatient.age" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Profile</label>
            <input v-model="localPatient.profile" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Address</label>
            <input v-model="localPatient.address" class="form-control">
          </div>

          
          <div class="mb-3">
            <label class="form-label">Contact</label>
            <input v-model="localPatient.contact" class="form-control">
          </div>

          


          
          


        </div>

        <div class="modal-footer">
          <button class="btn btn-secondary" @click="$emit('close')">Close</button>
          <button class="btn btn-success" @click="saveChanges">Save Changes</button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["patient"],
  data() {
    return {
      localPatient: { ...this.patient }
    };
  },
  methods: {
    async saveChanges() {
      const response = await fetch(`/api/patient/${this.localPatient.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem('adminToken')}`
        },
        body: JSON.stringify(this.localPatient)
      });

      const result = await response.json();
      if (response.ok) {
        alert("Patient updated successfully!");
        this.$emit("updated");
      } else {
        alert(result.message);
      }
    }
  }
};
</script>
<style scoped> 
.modal-body {
  max-height: 70vh;
  overflow-y: auto;
}
</style>