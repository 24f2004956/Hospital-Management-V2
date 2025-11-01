<template>
  <div class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5);">
    <div class="modal-dialog modal-md">
      <div class="modal-content" v-if="localDepartment">

        <div class="modal-header">
          <h5 class="modal-title">Edit Department</h5>
          <button type="button" class="btn-close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">

          <div class="mb-3">
            <label class="form-label">Department Name</label>
            <input v-model="localDepartment.name" class="form-control">
          </div>

          <div class="mb-3">
            <label class="form-label">Description</label>
            <input v-model="localDepartment.description" class="form-control">
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
  props: ["department"],
  data() {
    return {
      localDepartment: { ...this.department } // ✅ Local copy to avoid direct mutation
    };
  },
  methods: {
    async saveChanges() {
      const response = await fetch(`/api/department/${this.localDepartment.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${localStorage.getItem('adminToken')}`
        },
        body: JSON.stringify(this.localDepartment)
      });

      const result = await response.json();
      if (response.ok) {
        alert("Department updated successfully!");
        this.$emit("updated");
      } else {
        alert(result.message);
      }
    }
  }
};
</script>
