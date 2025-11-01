<template>
  <div class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-lg">
      <div class="modal-content" v-if="localDoctor">

        <div class="modal-header">
          <h5 class="modal-title">Edit Doctor</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">

          <div class="mb-3">
            <label class="form-label">Name</label>
            <input v-model="localDoctor.name" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Email</label>
            <input v-model="localDoctor.email" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Contact</label>
            <input v-model="localDoctor.contact" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Department</label>
            <select v-model="localDoctor.department_id" class="form-control">
              <option v-for="d in departments" :key="d.id" :value="d.id">
                {{ d.name }}
              </option>
            </select>
          </div>

          <div class="mb-3">
            <label class="form-label">Experience (Years)</label>
            <input type="number" v-model="localDoctor.experience_years" class="form-control">
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
  props: ["doctor", "departments"],
  data() {
    return {
      localDoctor: { ...this.doctor } // ✅ Avoid direct mutation
    };
  },
  methods: {
    async saveChanges() {
      const response = await fetch(`/api/doctor/${this.localDoctor.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem('adminToken')}`
        },
        body: JSON.stringify(this.localDoctor)
      });

      const result = await response.json();
      if (response.ok) {
        alert("Doctor updated successfully!");
        this.$emit("updated");
      } else {
        alert(result.message);
      }
    }
  }
};
</script>
