<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm px-3">
        <a class="navbar-brand fw-bold" href="#">Patient Dashboard</a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item"><router-link to="/" class="nav-link">Home</router-link></li>
                <li class="nav-item"><router-link to="/patient-profile-update" class="nav-link">Edit Profile</router-link></li>
                <li class="nav-item"><router-link to="/history-export" class="nav-link">History</router-link></li>
                <li class="nav-item"><button class="nav-link text-danger" @click="logout">Logout</button></li>
            </ul>
        </div>
    </nav>
</template> 

<script>
export default{
    name: 'PatientDashboard',
    data() {
        return {};
    },
    methods: {
        logout() {
            localStorage.removeItem('patientToken');
            this.$router.push('/patient-login');
        }
    },

}
</script>