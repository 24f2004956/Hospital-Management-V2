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
    }

  ],
})

export default router
