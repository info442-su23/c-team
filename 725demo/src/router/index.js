/*
 * @Author: Corn
 * @Date: 2023-07-25 16:06:18
 * @LastEditors: corn
 * @LastEditTime: 2023-07-26 14:46:40
 * @FilePath: \725demo\src\router\index.js
 * @Description: 
 * 
 * Copyright (c) 2023 by corn, All Rights Reserved. 
 */
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
      },
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import("@/views/Login")
  },
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
