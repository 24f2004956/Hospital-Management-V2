<template>
  <div class="modal fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5)">
    <div class="modal-dialog">
      <div class="modal-content">

        <div class="modal-header">
          <h5 class="modal-title">{{ doctor.name }} - Profile</h5>
          <button class="btn-close" @click="$emit('close')"></button>
        </div>

        <div class="modal-body">
          <p><strong>Experience:</strong> {{ doctor.experience_years || "N/A" }} Years</p>
          <p><strong>Qualification:</strong> {{ doctor.qualification || "N/A" }}</p>
          <p><strong>Contact:</strong> {{ doctor.contact }}</p>
        </div>

        <div class="modal-footer">
          <button class="btn btn-secondary" @click="$emit('close')">Close</button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default { props: ["doctor"] };
</script>
