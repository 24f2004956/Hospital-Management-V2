<template>
  <div class="hospital-home">
    <!-- Animated background elements -->
    <div class="background-container">
      <div class="bg-orb orb-1"></div>
      <div class="bg-orb orb-2"></div>
      <div class="bg-orb orb-3"></div>
    </div>

    <div class="content-wrapper">
      <!-- Header -->
      <div class="header">
        <div class="icon-wrapper">
          <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
          </svg>
        </div>
        <h1 class="title">
          Hospital Management
          <span class="title-gradient">System</span>
        </h1>
        <p class="subtitle">
          Streamlined healthcare management for better patient care
        </p>
      </div>

      <!-- Stats -->
      <div class="stats-grid">
        <div class="stat-card" v-for="(stat, index) in stats" :key="index" :style="{ animationDelay: `${index * 100}ms` }">
          <div class="stat-icon" :class="stat.colorClass">
            <component :is="stat.icon" />
          </div>
          <span class="stat-label">{{ stat.label }}</span>
        </div>
      </div>

      <!-- Role Cards -->
      <div class="roles-grid">
        <router-link
          v-for="(role, index) in roles"
          :key="role.id"
          :to="role.path"
          class="role-card"
          :class="{ 'hovered': hoveredCard === role.id }"
          @mouseenter="hoveredCard = role.id"
          @mouseleave="hoveredCard = null"
          :style="{ animationDelay: `${index * 150}ms` }"
        >
          <!-- Gradient overlay -->
          <div class="gradient-overlay" :class="hoveredCard === role.id ? role.hoverGradient : role.gradient"></div>
          
          <!-- Content -->
          <div class="role-content">
            <div class="role-icon" :class="role.gradient">
              <component :is="role.icon" />
            </div>
            
            <h3 class="role-title">{{ role.title }}</h3>
            
            <p class="role-description">{{ role.description }}</p>
            
            <div class="role-cta">
              <span>Access Portal</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="arrow-icon">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </div>
          </div>

          <!-- Decorative element -->
          <div class="decorative-circle"></div>
        </router-link>
      </div>

      <!-- Footer -->
      <div class="footer">
        <p>Secure • HIPAA Compliant • 24/7 Support</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data() {
    return {
      hoveredCard: null,
      stats: [
        { 
          icon: 'UsersIcon', 
          label: '10K+ Patients', 
          colorClass: 'text-blue' 
        },
        { 
          icon: 'StethoscopeIcon', 
          label: '500+ Doctors', 
          colorClass: 'text-emerald' 
        },
        { 
          icon: 'ClockIcon', 
          label: '24/7 Service', 
          colorClass: 'text-violet' 
        }
      ],
      roles: [
        {
          id: 'admin',
          title: 'Admin Portal',
          description: 'Manage hospital operations, staff, and resources',
          icon: 'ShieldIcon',
          gradient: 'gradient-blue',
          hoverGradient: 'gradient-blue-hover',
          path: '/admin-login'
        },
        {
          id: 'patient',
          title: 'Patient Portal',
          description: 'Book appointments, view records, and manage health',
          icon: 'HeartIcon',
          gradient: 'gradient-emerald',
          hoverGradient: 'gradient-emerald-hover',
          path: '/patient-login'
        },
        {
          id: 'doctor',
          title: 'Doctor Portal',
          description: 'Access patient records, schedules, and diagnostics',
          icon: 'StethoscopeIcon',
          gradient: 'gradient-violet',
          hoverGradient: 'gradient-violet-hover',
          path: '/doctor-login'
        }
      ]
    };
  },
  components: {
    UsersIcon: {
      template: `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
          <circle cx="9" cy="7" r="4"></circle>
          <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
          <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
        </svg>
      `
    },
    StethoscopeIcon: {
      template: `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4.8 2.3A.3.3 0 1 0 5 2H4a2 2 0 0 0-2 2v5a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6V4a2 2 0 0 0-2-2h-1a.2.2 0 1 0 .3.3"></path>
          <path d="M8 15v1a6 6 0 0 0 6 6v0a6 6 0 0 0 6-6v-4"></path>
          <circle cx="20" cy="10" r="2"></circle>
        </svg>
      `
    },
    ClockIcon: {
      template: `
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"></circle>
          <polyline points="12 6 12 12 16 14"></polyline>
        </svg>
      `
    },
    ShieldIcon: {
      template: `
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
        </svg>
      `
    },
    HeartIcon: {
      template: `
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
        </svg>
      `
    }
  }
};
</script>

<style scoped>
.hospital-home {
  min-height: 100vh;
  background: linear-gradient(to bottom right, #f8fafc, #eff6ff, #ecfeff);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  position: relative;
  overflow: hidden;
}

/* Animated background */
.background-container {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
}

.bg-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  animation: pulse 4s ease-in-out infinite;
}

.orb-1 {
  top: 5rem;
  left: 2.5rem;
  width: 18rem;
  height: 18rem;
  background-color: rgba(96, 165, 250, 0.1);
}

.orb-2 {
  bottom: 5rem;
  right: 2.5rem;
  width: 24rem;
  height: 24rem;
  background-color: rgba(34, 211, 238, 0.1);
  animation-delay: 1s;
}

.orb-3 {
  top: 50%;
  left: 50%;
  width: 20rem;
  height: 20rem;
  background-color: rgba(167, 139, 250, 0.1);
  animation-delay: 2s;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.8; transform: scale(1.1); }
}

/* Content wrapper */
.content-wrapper {
  max-width: 72rem;
  width: 100%;
  position: relative;
  z-index: 10;
}

/* Header */
.header {
  text-align: center;
  margin-bottom: 3rem;
  animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.icon-wrapper {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 5rem;
  height: 5rem;
  background: linear-gradient(to bottom right, #2563eb, #0891b2);
  border-radius: 1rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3);
  color: white;
}

.title {
  font-size: 3rem;
  font-weight: bold;
  color: #1e293b;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.title-gradient {
  display: block;
  background: linear-gradient(to right, #2563eb, #0891b2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-top: 0.5rem;
}

.subtitle {
  font-size: 1.25rem;
  color: #475569;
  max-width: 42rem;
  margin: 0 auto;
}

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border-radius: 1rem;
  padding: 1.5rem;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  display: flex;
  align-items: center;
  gap: 1rem;
  transition: all 0.3s ease;
  animation: fadeIn 0.8s ease-out;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

.stat-icon {
  padding: 0.75rem;
  border-radius: 0.75rem;
  background: #f8fafc;
}

.stat-icon svg {
  width: 1.5rem;
  height: 1.5rem;
}

.text-blue { color: #2563eb; }
.text-emerald { color: #059669; }
.text-violet { color: #7c3aed; }

.stat-label {
  font-size: 1.125rem;
  font-weight: 600;
  color: #334155;
}

/* Roles Grid */
.roles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.role-card {
  position: relative;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 1.5rem;
  padding: 2rem;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.5);
  text-decoration: none;
  overflow: hidden;
  transition: all 0.5s ease;
  animation: fadeIn 0.8s ease-out;
}

.role-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.gradient-overlay {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.role-card.hovered .gradient-overlay {
  opacity: 1;
}

.gradient-blue { background: linear-gradient(to bottom right, #2563eb, #0891b2); }
.gradient-blue-hover { background: linear-gradient(to bottom right, #1d4ed8, #0e7490); }
.gradient-emerald { background: linear-gradient(to bottom right, #059669, #0d9488); }
.gradient-emerald-hover { background: linear-gradient(to bottom right, #047857, #0f766e); }
.gradient-violet { background: linear-gradient(to bottom right, #7c3aed, #9333ea); }
.gradient-violet-hover { background: linear-gradient(to bottom right, #6d28d9, #7e22ce); }

.role-content {
  position: relative;
  z-index: 10;
}

.role-icon {
  display: inline-flex;
  padding: 1rem;
  border-radius: 1rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  transition: transform 0.5s ease;
  color: white;
}

.role-card:hover .role-icon {
  transform: scale(1.1);
}

.role-title {
  font-size: 1.5rem;
  font-weight: bold;
  color: #1e293b;
  margin-bottom: 0.75rem;
  transition: color 0.3s ease;
}

.role-card.hovered .role-title {
  color: white;
}

.role-description {
  color: #475569;
  margin-bottom: 1.5rem;
  line-height: 1.6;
  transition: color 0.3s ease;
}

.role-card.hovered .role-description {
  color: rgba(255, 255, 255, 0.9);
}

.role-cta {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #334155;
  font-weight: 600;
  transition: color 0.3s ease;
}

.role-card.hovered .role-cta {
  color: white;
}

.arrow-icon {
  transition: transform 0.3s ease;
}

.role-card:hover .arrow-icon {
  transform: translateX(0.5rem);
}

.decorative-circle {
  position: absolute;
  bottom: -3rem;
  right: -3rem;
  width: 8rem;
  height: 8rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  filter: blur(40px);
  transition: transform 0.7s ease;
}

.role-card:hover .decorative-circle {
  transform: scale(1.5);
}

/* Footer */
.footer {
  text-align: center;
  color: #64748b;
  font-size: 0.875rem;
}

/* Responsive */
@media (max-width: 768px) {
  .title {
    font-size: 2rem;
  }
  
  .subtitle {
    font-size: 1rem;
  }
  
  .roles-grid {
    grid-template-columns: 1fr;
  }
}
</style>