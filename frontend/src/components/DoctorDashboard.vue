<template>
    <!-- Modern Navbar with Gradient -->
    <nav class="navbar navbar-expand-lg navbar-dark shadow-lg" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
        <div class="container-fluid px-4">
            <a class="navbar-brand d-flex align-items-center" href="#">
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-heart-pulse-fill me-2" viewBox="0 0 16 16">
                    <path d="M1.475 9C2.702 10.84 4.779 12.871 8 15c3.221-2.129 5.298-4.16 6.525-6H12a.5.5 0 0 1-.464-.314l-1.457-3.642-1.598 5.593a.5.5 0 0 1-.945.049L5.889 6.568l-1.473 2.21A.5.5 0 0 1 4 9H1.475Z"/>
                    <path d="M.88 8C-2.427 1.68 4.41-2 7.823 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C11.59-2 18.426 1.68 15.12 8h-2.783l-1.874-4.686a.5.5 0 0 0-.945.049L7.921 8.956 6.464 5.314a.5.5 0 0 0-.88-.091L3.732 8H.88Z"/>
                </svg>
                <span class="fw-bold fs-4">Doctor Portal</span>
            </a>

            <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav ms-auto align-items-lg-center gap-3">
                    <li class="nav-item">
                        <span class="text-white opacity-75">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle me-1" viewBox="0 0 16 16">
                                <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                                <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                            </svg>
                            Hello, <strong>{{ username }}</strong>
                        </span>
                    </li>
                    <li class="nav-item">
                        <router-link to="/doctor-profile-update" class="btn btn-outline-light btn-sm">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square me-1" viewBox="0 0 16 16">
                                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                            </svg>
                            Edit Profile
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <router-link to="/doctor-availability" class="btn btn-outline-light btn-sm">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar-check me-1" viewBox="0 0 16 16">
                                <path d="M10.854 7.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 9.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                                <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                            </svg>
                            Availability
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <button class="btn btn-danger btn-sm" @click="logout">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-box-arrow-right me-1" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
                                <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
                            </svg>
                            Logout
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content Area -->
    <div class="container-fluid px-4 py-5" style="background-color: #f8f9fa; min-height: 100vh;">
        

        <div class="row g-4">
            <!-- Upcoming Appointments Card -->
            <div class="col-12 col-xl-7">
                <div class="card border-0 shadow-sm rounded-3 h-100">
                    <div class="card-header bg-white border-0 py-3">
                        <h3 class="mb-0 fw-bold text-primary">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-clock-history me-2" viewBox="0 0 16 16">
                                <path d="M8.515 1.019A7 7 0 0 0 8 1V0a8 8 0 0 1 .589.022l-.074.997zm2.004.45a7.003 7.003 0 0 0-.985-.299l.219-.976c.383.086.76.2 1.126.342l-.36.933zm1.37.71a7.01 7.01 0 0 0-.439-.27l.493-.87a8.025 8.025 0 0 1 .979.654l-.615.789a6.996 6.996 0 0 0-.418-.302zm1.834 1.79a6.99 6.99 0 0 0-.653-.796l.724-.69c.27.285.52.59.747.91l-.818.576zm.744 1.352a7.08 7.08 0 0 0-.214-.468l.893-.45a7.976 7.976 0 0 1 .45 1.088l-.95.313a7.023 7.023 0 0 0-.179-.483zm.53 2.507a6.991 6.991 0 0 0-.1-1.025l.985-.17c.067.386.106.778.116 1.17l-1 .025zm-.131 1.538c.033-.17.06-.339.081-.51l.993.123a7.957 7.957 0 0 1-.23 1.155l-.964-.267c.046-.165.086-.332.12-.501zm-.952 2.379c.184-.29.346-.594.486-.908l.914.405c-.16.36-.345.706-.555 1.038l-.845-.535zm-.964 1.205c.122-.122.239-.248.35-.378l.758.653a8.073 8.073 0 0 1-.401.432l-.707-.707z"/>
                                <path d="M8 1a7 7 0 1 0 4.95 11.95l.707.707A8.001 8.001 0 1 1 8 0v1z"/>
                                <path d="M7.5 3a.5.5 0 0 1 .5.5v5.21l3.248 1.856a.5.5 0 0 1-.496.868l-3.5-2A.5.5 0 0 1 7 9V3.5a.5.5 0 0 1 .5-.5z"/>
                            </svg>
                            Upcoming Appointments
                        </h3>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive">
                            <table class="table table-hover mb-0" v-if="appointments.length">
                                <thead style="background-color: #f8f9fa;">
                                    <tr>
                                        <th class="text-center py-3" style="width: 60px;">#</th>
                                        <th class="py-3">Patient Name</th>
                                        <th class="text-center py-3">Medical History</th>
                                        <th class="text-center py-3" style="min-width: 250px;">Actions</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(appointment, index) in appointments" :key="appointment.id">
                                        <td class="text-center align-middle">
                                            <span class="badge bg-light text-dark">{{ index + 1 }}</span>
                                        </td>
                                        <td class="align-middle">
                                            <div class="d-flex align-items-center">
                                                <div class="bg-primary bg-opacity-10 rounded-circle p-2 me-2">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-fill text-primary" viewBox="0 0 16 16">
                                                        <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3Zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"/>
                                                    </svg>
                                                </div>
                                                <strong>{{ appointment.patient_name }}</strong>
                                            </div>
                                        </td>
                                        <td class="text-center align-middle">
                                            <button class="btn btn-sm btn-outline-info" @click="updatePatientHistory(appointment)">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-pencil me-1" viewBox="0 0 16 16">
                                                    <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
                                                </svg>
                                                Update
                                            </button>
                                        </td>
                                        <td class="text-center align-middle">
                                            <div class="btn-group" role="group">
                                                <button class="btn btn-sm btn-success" @click="completeAppointment(appointment)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-check-circle me-1" viewBox="0 0 16 16">
                                                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                                        <path d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z"/>
                                                    </svg>
                                                    Complete
                                                </button>
                                                <button class="btn btn-sm btn-danger" @click="cancelAppointment(appointment)">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-x-circle me-1" viewBox="0 0 16 16">
                                                        <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
                                                        <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
                                                    </svg>
                                                    Cancel
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div v-if="!appointments.length" class="text-center py-5">
                            <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" class="bi bi-calendar-x text-muted mb-3" viewBox="0 0 16 16">
                                <path d="M6.146 7.146a.5.5 0 0 1 .708 0L8 8.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 9l1.147 1.146a.5.5 0 0 1-.708.708L8 9.707l-1.146 1.147a.5.5 0 0 1-.708-.708L7.293 9 6.146 7.854a.5.5 0 0 1 0-.708z"/>
                                <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                            </svg>
                            <p class="text-muted fs-5">No upcoming appointments</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Assigned Patients Card -->
            <div class="col-12 col-xl-5">
                <div class="card border-0 shadow-sm rounded-3 h-100">
                    <div class="card-header bg-white border-0 py-3">
                        <h3 class="mb-0 fw-bold text-success">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-people-fill me-2" viewBox="0 0 16 16">
                                <path d="M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1H7Zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm-5.784 6A2.238 2.238 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.325 6.325 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1h4.216ZM4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z"/>
                            </svg>
                            Assigned Patients
                        </h3>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive">
                            <table class="table table-hover mb-0" v-if="assignedPatients.length">
                                <thead style="background-color: #f8f9fa;">
                                    <tr>
                                        <th class="text-center py-3" style="width: 60px;">#</th>
                                        <th class="py-3">Name</th>
                                        <th class="py-3">Email</th>
                                        <th class="text-center py-3">Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(patient, index) in assignedPatients" :key="patient.id">
                                        <td class="text-center align-middle">
                                            <span class="badge bg-light text-dark">{{ index + 1 }}</span>
                                        </td>
                                        <td class="align-middle">
                                            <div class="d-flex align-items-center">
                                                <div class="bg-success bg-opacity-10 rounded-circle p-2 me-2">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-fill text-success" viewBox="0 0 16 16">
                                                        <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3Zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"/>
                                                    </svg>
                                                </div>
                                                <strong>{{ patient.name }}</strong>
                                            </div>
                                        </td>
                                        <td class="align-middle">
                                            <small class="text-muted">{{ patient.email }}</small>
                                        </td>
                                        <td class="text-center align-middle">
                                            <button class="btn btn-sm btn-outline-primary" @click="openPatientHistory(patient)">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-file-medical me-1" viewBox="0 0 16 16">
                                                    <path d="M8.5 4.5a.5.5 0 0 0-1 0v.634l-.549-.317a.5.5 0 1 0-.5.866L7 6l-.549.317a.5.5 0 1 0 .5.866l.549-.317V7.5a.5.5 0 1 0 1 0v-.634l.549.317a.5.5 0 1 0 .5-.866L9 6l.549-.317a.5.5 0 1 0-.5-.866l-.549.317V4.5zM5.5 9a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5zm0 2a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5z"/>
                                                    <path d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2zm10-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1z"/>
                                                </svg>
                                                View History
                                            </button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div v-if="!assignedPatients.length" class="text-center py-5">
                            <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" class="bi bi-person-x text-muted mb-3" viewBox="0 0 16 16">
                                <path d="M11 5a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm.256 7a4.474 4.474 0 0 1-.229-1.004H3c.001-.246.154-.986.832-1.664C4.484 10.68 5.711 10 8 10c.26 0 .507.009.74.025.226-.341.496-.65.804-.918C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4s1 1 1 1h5.256Zm3.63-4.54c.18-.613 1.048-.613 1.229 0l.043.148a.64.64 0 0 0 .921.382l.136-.074c.561-.306 1.175.308.87.869l-.075.136a.64.64 0 0 0 .382.92l.149.045c.612.18.612 1.048 0 1.229l-.15.043a.64.64 0 0 0-.38.921l.074.136c.305.561-.309 1.175-.87.87l-.136-.075a.64.64 0 0 0-.92.382l-.045.149c-.18.612-1.048.612-1.229 0l-.043-.15a.64.64 0 0 0-.921-.38l-.136.074c-.561.305-1.175-.309-.87-.87l.075-.136a.64.64 0 0 0-.382-.92l-.148-.045c-.613-.18-.613-1.048 0-1.229l.148-.043a.64.64 0 0 0 .382-.921l-.074-.136c-.306-.561.308-1.175.869-.87l.136.075a.64.64 0 0 0 .92-.382l.045-.148ZM14 12.5a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0Z"/>
                            </svg>
                            <p class="text-muted fs-5">No assigned patients yet</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Modals -->
    <UpdatePatientHistory :show="showHistoryModal" :appointmentId="selectedAppointmentId" @close="closeModal" />
    <PatientHistory v-if="showPatientHistoryModal" :patient="selectedPatient" @close="showPatientHistoryModal = false" />
</template>


<script>
import UpdatePatientHistory from './UpdatePatientHistory.vue';
import PatientHistory from './PatientHistory.vue';
export default {
    name: 'DoctorDashboard',
    data() {
        return {
            username: localStorage.getItem("username") || "",
            appointments: [],
            showHistoryModal: false,
            selectedPatient: null,
            showPatientHistoryModal: false,
            assignedPatients: [],
            errorMessage: null,
            selectedAppointmentId: null
        }

    },
    components: {
        UpdatePatientHistory, PatientHistory
    },
    methods: {
        logout() {
            localStorage.removeItem('doctorToken');
            this.$router.push('/');
        },

        async fetchAppointments() {
            try {
                const response = await fetch('/api/appointment', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('doctorToken')}`
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

        async completeAppointment(appointment) {
            try {
                const response = await fetch(`/api/appointment/${appointment.id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('doctorToken')}`
                    },
                    body: JSON.stringify({ status: "Completed" })
                });

                const result = await response.json();

                if (!response.ok) {
                    alert(result.message);
                } else {
                    alert("Appointment marked as Completed");
                    this.fetchAppointments();
                }
            } catch (error) {
                alert("Server error while updating appointment.");
            }
        },

        async cancelAppointment(appointment) {
            const reason = prompt("Enter cancellation reason:");
            if (!reason) return;

            try {
                const response = await fetch(`/api/appointment/${appointment.id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${localStorage.getItem('doctorToken')}`
                    },
                    body: JSON.stringify({
                        status: "Cancelled",
                        reason: reason
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
        async fetchAssignedPatients() {
            const response = await fetch('/api/patient', {
                headers: {
                    "Authorization": `Bearer ${localStorage.getItem('doctorToken')}`
                }
            });

            this.assignedPatients = await response.json();
        },
        openPatientHistory(patient) {
            this.selectedPatient = patient;
            this.showPatientHistoryModal = true;
        },

        updatePatientHistory(appointment) {
            this.selectedAppointmentId = appointment.id;
            this.showHistoryModal = true;
        },
        closeModal() {
            this.showHistoryModal = false;
        },


    },
    mounted() {
        this.fetchAppointments();
        this.fetchAssignedPatients();
    },

}
</script>

<style scoped>
/* Smooth transitions for all interactive elements */
* {
    transition: all 0.3s ease;
}

/* Navbar styling */
.navbar {
    backdrop-filter: blur(10px);
}

.navbar-brand {
    font-size: 1.5rem;
    letter-spacing: -0.5px;
}

.navbar-brand:hover {
    transform: scale(1.05);
}

/* Button hover effects */
.btn {
    font-weight: 500;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.btn:active {
    transform: translateY(0);
}

.btn-outline-light:hover {
    background-color: rgba(255, 255, 255, 0.2);
    border-color: rgba(255, 255, 255, 0.8);
}

/* Card styling */
.card {
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1) !important;
}

.card-header {
    border-bottom: 3px solid #f8f9fa;
}

/* Table styling */
.table {
    border-collapse: separate;
    border-spacing: 0;
}

.table thead th {
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    border-bottom: 2px solid #dee2e6;
}

.table tbody tr {
    transition: all 0.2s ease;
}

.table-hover tbody tr:hover {
    background-color: #f8f9fa;
    transform: scale(1.01);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.table tbody tr:last-child td {
    border-bottom: none;
}

/* Badge styling */
.badge {
    padding: 0.5rem 0.75rem;
    font-weight: 600;
    font-size: 0.875rem;
}

/* Icon container styling */
.bg-primary.bg-opacity-10,
.bg-success.bg-opacity-10 {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Button group styling */
.btn-group .btn {
    margin: 0 2px;
}

.btn-sm {
    padding: 0.4rem 0.8rem;
    font-size: 0.875rem;
}

/* Empty state styling */
.text-center svg {
    opacity: 0.3;
    animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: scale(0.9);
    }
    to {
        opacity: 0.3;
        transform: scale(1);
    }
}

/* Export button special styling */
.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    font-weight: 600;
    padding: 0.6rem 1.5rem;
}

.btn-primary:hover {
    background: linear-gradient(135deg, #5568d3 0%, #63398b 100%);
}

/* Success button styling */
.btn-success {
    background-color: #10b981;
    border-color: #10b981;
}

.btn-success:hover {
    background-color: #059669;
    border-color: #059669;
}

/* Danger button styling */
.btn-danger {
    background-color: #ef4444;
    border-color: #ef4444;
}

.btn-danger:hover {
    background-color: #dc2626;
    border-color: #dc2626;
}

/* Outline button variants */
.btn-outline-info {
    color: #0ea5e9;
    border-color: #0ea5e9;
}

.btn-outline-info:hover {
    background-color: #0ea5e9;
    border-color: #0ea5e9;
    color: white;
}

.btn-outline-primary {
    color: #667eea;
    border-color: #667eea;
}

.btn-outline-primary:hover {
    background-color: #667eea;
    border-color: #667eea;
    color: white;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .navbar-brand {
        font-size: 1.2rem;
    }
    
    .card:hover {
        transform: none;
    }
    
    .table-hover tbody tr:hover {
        transform: none;
    }
    
    .btn-group {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }
    
    .btn-group .btn {
        width: 100%;
        margin: 0;
    }
}

/* Smooth scroll behavior */
html {
    scroll-behavior: smooth;
}

/* Custom scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb {
    background: #667eea;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #5568d3;
}

/* Loading animation for tables */
.table tbody tr {
    animation: slideIn 0.3s ease-out forwards;
    opacity: 0;
}

.table tbody tr:nth-child(1) { animation-delay: 0.1s; }
.table tbody tr:nth-child(2) { animation-delay: 0.2s; }
.table tbody tr:nth-child(3) { animation-delay: 0.3s; }
.table tbody tr:nth-child(4) { animation-delay: 0.4s; }
.table tbody tr:nth-child(5) { animation-delay: 0.5s; }

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>


