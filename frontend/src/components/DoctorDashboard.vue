<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm px-3">
        <a class="navbar-brand fw-bold" href="#">Doctor Dashboard</a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">Hello {{ username }} !</li>
                <li class="nav-item"><router-link to="/doctor-profile-update" class="nav-link">Edit
                        Profile</router-link></li>
                <li class="nav-item"><router-link to="/doctor-availability" class="nav-link">Provide
                        Availability</router-link></li>
                <li class="nav-item"><button class="nav-link text-danger" @click="logout">Logout</button></li>
            </ul>
        </div>
    </nav>
    <button @click="downloadPDF" class="btn btn-primary">Export Report as PDF</button>


    <div>
        <div>
            <h3 class="mb-4 text-center">Upcoming Appointments</h3>

            <table class="table table-bordered table-striped text-center shadow-sm" v-if="appointments.length">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Patient</th>
                        <th>PatientHistory</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(appointment, index) in appointments" :key="appointment.id">
                        <td>{{ index + 1 }}</td>
                        <td>{{ appointment.patient_name }}</td>
                        <td>
                            <button class="btn btn-success btn-sm"
                                @click="updatePatientHistory(appointment)">Update</button>
                        </td>
                        <td>
                            <button class="btn btn-success btn-sm" @click="completeAppointment(appointment)">Mark as
                                Complete</button>
                            <button class="btn btn-danger btn-sm"
                                @click="cancelAppointment(appointment)">Cancel</button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p v-else class="text-center text-muted mt-3">No upcoming appointments.</p>
        </div>

        <div>
            <h3 class="mb-4 text-center">Assigned Patients</h3>
            <table class="table table-bordered text-center" v-if="assignedPatients.length">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(patient, index) in assignedPatients" :key="patient.id">
                        <td>{{ index + 1 }}</td>
                        <td>{{ patient.name }}</td>
                        <td>{{ patient.email }}</td>
                        <td>
                            <button class="btn btn-primary" @click="openPatientHistory(patient)">View History</button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p v-else class="text-center text-muted mt-3">No assigned patients yet.</p>
        </div>
    </div>
    <UpdatePatientHistory :show="showHistoryModal" :appointmentId="selectedAppointmentId" @close="closeModal" />
    <PatientHistory v-if="showPatientHistoryModal" :patient="selectedPatient"
        @close="showPatientHistoryModal = false" />

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
        async downloadPDF() {
    const month = "2025-01"; // You can use a date picker to make dynamic

    const response = await fetch(`/api/reports/monthly?month=${month}`, {
      method: 'GET',
    });

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `Monthly_Report_${month}.pdf`;
    a.click();
    window.URL.revokeObjectURL(url);
  },
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