<template>
    <!-- Modern Navigation -->
    <nav class="modern-navbar">
        <div class="navbar-container">
            <div class="navbar-brand">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
                </svg>
                <span>Patient Portal</span>
            </div>

            <button class="mobile-toggle" @click="mobileMenuOpen = !mobileMenuOpen">
                <span></span>
                <span></span>
                <span></span>
            </button>

            <div class="navbar-menu" :class="{ 'is-active': mobileMenuOpen }">
                <div class="user-greeting">
                    <div class="user-avatar">{{ username.charAt(0).toUpperCase() }}</div>
                    <span class="username">{{ username }}</span>
                </div>

                <router-link to="/patient-profile-update" class="nav-link">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                        <circle cx="12" cy="7" r="4"/>
                    </svg>
                   Edit Profile
                </router-link>

                <router-link to="/history-export" class="nav-link">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M12 20h9"/>
                        <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>
                    </svg>
                    History
                </router-link>

                <button class="nav-link logout-btn" @click="logout">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
                        <polyline points="16 17 21 12 16 7"/>
                        <line x1="21" y1="12" x2="9" y2="12"/>
                    </svg>
                    Logout
                </button>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="dashboard-content">
        <!-- Welcome Section -->
        <div class="welcome-section">
            <div class="welcome-card">
                <h1>Welcome back, {{ username }}! 👋</h1>
                <p>Manage your appointments and explore healthcare services</p>
            </div>
        </div>

        <!-- Departments Section -->
        <div v-if="departments.length" class="section">
            <div class="section-header">
                <h2>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="7" height="7"/>
                        <rect x="14" y="3" width="7" height="7"/>
                        <rect x="14" y="14" width="7" height="7"/>
                        <rect x="3" y="14" width="7" height="7"/>
                    </svg>
                    Healthcare Departments
                </h2>
                <span class="badge">{{ departments.length }} Available</span>
            </div>

            <div class="departments-grid">
                <div 
                    v-for="(department, index) in departments" 
                    :key="department.id"
                    class="department-card"
                >
                    <div class="department-icon">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20 6L9 17l-5-5"/>
                        </svg>
                    </div>
                    <h3>{{ department.name }}</h3>
                    <button class="view-btn" @click="department_details(department.id)">
                        View Details
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M5 12h14M12 5l7 7-7 7"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <div v-else class="empty-state">
            <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                <circle cx="12" cy="12" r="10"/>
                <line x1="12" y1="8" x2="12" y2="12"/>
                <line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
            <h3>No Departments Available</h3>
            <p>Check back later for available healthcare departments.</p>
        </div>

        <!-- Appointments Section -->
        <div class="section">
            <div class="section-header">
                <h2>
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                        <line x1="16" y1="2" x2="16" y2="6"/>
                        <line x1="8" y1="2" x2="8" y2="6"/>
                        <line x1="3" y1="10" x2="21" y2="10"/>
                    </svg>
                    Upcoming Appointments
                </h2>
                <span class="badge" v-if="appointments.length">{{ appointments.length }}</span>
            </div>

            <div v-if="appointments.length" class="appointments-list">
                <div 
                    v-for="(appointment, index) in appointments" 
                    :key="appointment.id"
                    class="appointment-card"
                >
                    <div class="appointment-left">
                        <div class="appointment-number">{{ index + 1 }}</div>
                        <div class="appointment-details">
                            <h4>{{ appointment.doctor_name }}</h4>
                            <p class="department">{{ appointment.department_name }}</p>
                            <div class="appointment-meta">
                                <span class="meta-item">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                                        <line x1="16" y1="2" x2="16" y2="6"/>
                                        <line x1="8" y1="2" x2="8" y2="6"/>
                                        <line x1="3" y1="10" x2="21" y2="10"/>
                                    </svg>
                                    {{ appointment.date }}
                                </span>
                                <span class="meta-item">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <circle cx="12" cy="12" r="10"/>
                                        <polyline points="12 6 12 12 16 14"/>
                                    </svg>
                                    {{ appointment.time }}
                                </span>
                            </div>
                        </div>
                    </div>
                    <button class="cancel-btn" @click="cancelAppointment(appointment)">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <line x1="18" y1="6" x2="6" y2="18"/>
                            <line x1="6" y1="6" x2="18" y2="18"/>
                        </svg>
                        Cancel
                    </button>
                </div>
            </div>

            <div v-else class="empty-state">
                <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                    <line x1="16" y1="2" x2="16" y2="6"/>
                    <line x1="8" y1="2" x2="8" y2="6"/>
                    <line x1="3" y1="10" x2="21" y2="10"/>
                </svg>
                <h3>No Upcoming Appointments</h3>
                <p>You don't have any scheduled appointments yet.</p>
            </div>
        </div>
    </div>
</template>


<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Modern Navigation */
.modern-navbar {
    background: white;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    position: sticky;
    top: 0;
    z-index: 1000;
    border-bottom: 1px solid #e5e7eb;
}

.navbar-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 70px;
}

.navbar-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 20px;
    font-weight: 700;
    color: #1e293b;
}

.navbar-brand svg {
    color: #667eea;
}

.mobile-toggle {
    display: none;
    flex-direction: column;
    gap: 4px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
}

.mobile-toggle span {
    width: 24px;
    height: 2px;
    background: #64748b;
    border-radius: 2px;
    transition: all 0.3s ease;
}

.navbar-menu {
    display: flex;
    align-items: center;
    gap: 8px;
}

.user-greeting {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 16px;
    background: #f8fafc;
    border-radius: 10px;
    margin-right: 16px;
}

.user-avatar {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 14px;
}

.username {
    font-weight: 600;
    color: #1e293b;
}

.nav-link {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 10px 16px;
    color: #64748b;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    border-radius: 8px;
    transition: all 0.2s ease;
    border: none;
    background: transparent;
    cursor: pointer;
}

.nav-link:hover {
    background: #f1f5f9;
    color: #1e293b;
}

.logout-btn {
    color: #ef4444;
}

.logout-btn:hover {
    background: #fef2f2;
    color: #dc2626;
}

/* Main Content */
.dashboard-content {
    max-width: 1400px;
    margin: 0 auto;
    padding: 32px 24px;
    min-height: calc(100vh - 70px);
    background: linear-gradient(135deg, #f5f7fa 0%, #e8eef5 100%);
}

/* Welcome Section */
.welcome-section {
    margin-bottom: 32px;
}

.welcome-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 40px;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
}

.welcome-card h1 {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 8px;
}

.welcome-card p {
    font-size: 16px;
    opacity: 0.95;
}

/* Section */
.section {
    margin-bottom: 32px;
}

.section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
}

.section-header h2 {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 24px;
    font-weight: 700;
    color: #1e293b;
}

.badge {
    padding: 6px 14px;
    background: #667eea;
    color: white;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

/* Departments Grid */
.departments-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 20px;
}

.department-card {
    background: white;
    padding: 32px 24px;
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.department-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.department-icon {
    width: 64px;
    height: 64px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
}

.department-icon svg {
    color: white;
}

.department-card h3 {
    font-size: 18px;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 16px;
}

.view-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 10px 20px;
    background: #f8fafc;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    color: #475569;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

.view-btn:hover {
    background: #667eea;
    border-color: #667eea;
    color: white;
}

/* Appointments List */
.appointments-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.appointment-card {
    background: white;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.2s ease;
}

.appointment-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.appointment-left {
    display: flex;
    align-items: center;
    gap: 20px;
    flex: 1;
}

.appointment-number {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
}

.appointment-details h4 {
    font-size: 18px;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 4px;
}

.department {
    color: #667eea;
    font-weight: 500;
    font-size: 14px;
    margin-bottom: 8px;
}

.appointment-meta {
    display: flex;
    gap: 16px;
}

.meta-item {
    display: flex;
    align-items: center;
    gap: 6px;
    color: #64748b;
    font-size: 14px;
}

.cancel-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 10px 20px;
    background: #fef2f2;
    border: 2px solid #fee2e2;
    border-radius: 8px;
    color: #dc2626;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

.cancel-btn:hover {
    background: #dc2626;
    border-color: #dc2626;
    color: white;
}

/* Empty State */
.empty-state {
    background: white;
    padding: 60px 40px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.empty-state svg {
    color: #cbd5e1;
    margin-bottom: 20px;
}

.empty-state h3 {
    font-size: 20px;
    font-weight: 600;
    color: #475569;
    margin-bottom: 8px;
}

.empty-state p {
    color: #94a3b8;
    font-size: 14px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .mobile-toggle {
        display: flex;
    }

    .navbar-menu {
        position: fixed;
        top: 70px;
        left: -100%;
        width: 280px;
        height: calc(100vh - 70px);
        background: white;
        flex-direction: column;
        align-items: flex-start;
        padding: 24px;
        box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
        transition: left 0.3s ease;
        gap: 8px;
    }

    .navbar-menu.is-active {
        left: 0;
    }

    .user-greeting {
        width: 100%;
        margin-right: 0;
        margin-bottom: 16px;
    }

    .nav-link {
        width: 100%;
        justify-content: flex-start;
    }

    .welcome-card {
        padding: 24px;
    }

    .welcome-card h1 {
        font-size: 24px;
    }

    .departments-grid {
        grid-template-columns: 1fr;
    }

    .appointment-card {
        flex-direction: column;
        align-items: flex-start;
        gap: 16px;
    }

    .cancel-btn {
        width: 100%;
        justify-content: center;
    }
}
</style>

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