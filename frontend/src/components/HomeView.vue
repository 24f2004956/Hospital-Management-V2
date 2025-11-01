<template>
  <div class="d-flex justify-content-center align-items-center vh-100 bg-light">
    <div class="card shadow-lg rounded-4 p-4 text-center" style="max-width: 450px; width: 100%;">
      <h2 class="fw-semibold mb-3">🏥 Hospital Management System</h2>
      <p class="text-muted mb-4">Choose your role to continue</p>

      <div class="d-grid gap-3">
        <router-link to="/admin-login" class="btn btn-primary btn-lg rounded-pill">
          Admin Login
        </router-link>

        <router-link to="/patient-login" class="btn btn-success btn-lg rounded-pill">
          Patient Login
        </router-link>

        <router-link to="/doctor-login" class="btn btn-info btn-lg text-white rounded-pill">
          Doctor Login
        </router-link>
      </div>
    </div>
  </div>
</template>


<script>
export default{
    name:'HomeView',
    
}
</script>