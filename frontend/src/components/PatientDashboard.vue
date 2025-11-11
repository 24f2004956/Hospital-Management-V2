<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm px-3">
        <a class="navbar-brand fw-bold" href="#">Patient Dashboard</a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">Hello {{ username }} !</li>
                <li class="nav-item"><router-link to="/patient-profile-update" class="nav-link">Edit
                        Profile</router-link></li>
                <li class="nav-item"><router-link to="/history-export" class="nav-link">History</router-link></li>
                <li class="nav-item"><button class="nav-link text-danger" @click="logout">Logout</button></li>
            </ul>
        </div>
    </nav>

    <div v-if="departments.length" class="container mt-5">
        <h3 class="mb-4 text-center" id="department-section">Department List</h3>

        <table class="table table-bordered table-striped text-center shadow-sm">
            <thead class="table-dark">
                <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(department, index) in departments" :key="department.id">
                    <td>{{ index + 1 }}</td>
                    <td>{{ department.name }}</td>
                    <td>
                        <button class="btn btn-warning btn-sm" @click="department_details(department.id)">View</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div v-else class="text-center text-muted mt-5">
        <h5>No departments available at the moment.</h5>
    </div>

    <div>
        <h3 class="mb-4 text-center">Upcoming Appointments</h3>

        <table class="table table-bordered table-striped text-center shadow-sm" v-if="appointments.length">
            <thead class="table-dark">
                <tr>
                    <th>#</th>
                    <th>Doctor</th>
                    <th>Department</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(appointment, index) in appointments" :key="appointment.id">
                    <td>{{ index + 1 }}</td>
                    <td>{{ appointment.doctor_name }}</td>
                    <td>{{ appointment.department_name }}</td>
                    <td>{{ appointment.date }}</td>
                    <td>{{ appointment.time }}</td>
                    <td>
                        <button class="btn btn-danger btn-sm" @click="cancelAppointment(appointment)">Cancel</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <p v-else class="text-center text-muted mt-3">No upcoming appointments.</p>
    </div>
</template>

<script>
export default {
    name: 'PatientDashboard',
    data() {
        return {
            departments: [],
            appointments: [],
            username: localStorage.getItem("username") || "",
        };
    },
    methods: {
        logout() {
            localStorage.removeItem('patientToken');
            this.$router.push('/');
        },
        department_details(id) {
            this.$router.push(`/department-details/${id}`);
        },

        async fetchDepartments() {
            try {
                const response = await fetch('/api/department', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('patientToken')}`
                    }
                });
                const result = await response.json();
                if (!response.ok) {
                    this.errorMessage = result.message;
                } else {
                    this.departments = Array.isArray(result) ? result : [result];
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        },

        async fetchAppointments() {
            try {
                const response = await fetch('/api/appointment', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('patientToken')}`
                    }
                });
                const result = await response.json();
                if (!response.ok) {
                    this.errorMessage = result.message;
                } else {
                    this.appointments = result;
                }
            } catch (error) {
                this.errorMessage = 'Unable to connect to the server. Please try again later.';
            }
        },

        async cancelAppointment(appointment) {
            try {
                const response = await fetch(`/api/appointment/${appointment.id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('patientToken')}`
                    },
                    body: JSON.stringify({
                        status: "Cancelled",
                
                    })
                });

                const result = await response.json();

                if (!response.ok) {
                    alert(result.message);
                } else {
                    alert(" Appointment Cancelled");
                    this.fetchAppointments();
                }
            } catch (error) {
                alert("Server error while updating appointment.");
            }
        },
    },
    mounted() {
        this.fetchDepartments();
        this.fetchAppointments();
    }

}
</script>