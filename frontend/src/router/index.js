import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/components/HomeView.vue'
import AdminLogin from '@/components/AdminLogin.vue'
import PatientLogin from '@/components/PatientLogin.vue'
import DoctorLogin from '@/components/DoctorLogin.vue'
import PatientRegister from '@/components/PatientRegister.vue'
import AdminDashboard from '@/components/AdminDashboard.vue'
import DoctorRegister from '@/components/DoctorRegister.vue'
import BlackListed from '@/components/BlackListed.vue'
import CreateDepartment from '@/components/CreateDepartment.vue'
import DoctorDashboard from '@/components/DoctorDashboard.vue'
import DoctorAvailability from '@/components/DoctorAvailability.vue'
import PatientDashboard from '@/components/PatientDashboard.vue'
import PatienProfileUpdate from '@/components/PatienProfileUpdate.vue'
import HistoryExport from '@/components/HistoryExport.vue'
import ViewDepartment from '@/components/ViewDepartment.vue'
import DoctorProfileUpdate from '@/components/DoctorProfileUpdate.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/admin-login',
      name: 'admin-login',
      component: AdminLogin
    },
    {
      path: '/patient-login',
      name: 'patient-login',
      component: PatientLogin
    },
    {
      path: '/doctor-login',
      name: 'doctor-login',
      component: DoctorLogin
    },
    {
      path: '/patient-register',
      name: 'patient-register',
      component: PatientRegister
    },
    {
      path: '/admin-dashboard',
      name: 'admin-dashboard',
      component: AdminDashboard
    },
    {
      path: '/doctor-register',
      name: 'doctor-register',
      component: DoctorRegister
    },
    {
      path: '/blacklisted',
      name: 'blacklisted',
      component: BlackListed
    },
    {
      path: '/create-department',
      name: 'create-department',
      component: CreateDepartment
    },
    {
      path: '/doctor-dashboard',
      name: 'doctor-dashboard',
      component: DoctorDashboard,
    },
    {
      path: '/doctor-availability',
      name: 'doctor-availability',  
      component: DoctorAvailability,
    },
    {
      path: '/patient-dashboard',
      name: 'patient-dashboard',
      component: PatientDashboard,
    },
    {
      path: '/patient-profile-update',
      name: 'patient-profile-update',
      component: PatienProfileUpdate,
    },
    {
      path: '/history-export',
      name: 'history-export',
      component: HistoryExport,
    },
    {
      path: '/department-details/:id',
      name: 'department-details',
      component: ViewDepartment,
    },
    {
      path: '/doctor-profile-update',
      name: 'doctor-profile-update',
      component: DoctorProfileUpdate,
    },

  ],
})

export default router
