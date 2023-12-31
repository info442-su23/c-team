
import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from "@/layout/Layout";


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Layout',
    component: Layout,
    redirect: "/home",
    children: [
      {
        path: '/home',
        name: 'Home',
        component: () => import("@/views/HomeView"),
      },
      {
        path: '/listview',
        name: 'ListView',
        component: () => import("@/views/ListView"),
      },
      {
        path: '/listview2',
        name: 'ListView2',
        component: () => import("@/views/ListView2"),
      },
      {
        path: '/study',
        name: 'Study',
        component: () => import("@/views/Study"),
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import("@/views/Login")
  },
  {
    path: '/treepage',
    name: 'TreePage',
    component: () => import("@/views/TreePage"),
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
