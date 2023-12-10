'use client'
import React, { Suspense, useContext, useState } from 'react'
import RecentChats from '@/components/CommunicatePageComponents/RecentChats'
import MainChatCard from '@/components/CommunicatePageComponents/MainChatCard'
import HomeContext from '@/context/HomeContext'
import Loader from '@/components/ClipLoader'

export default function Projects() {
  const {EachUsersMessage,setEachUserMessage,auth} = useContext(HomeContext)
  
  return (
    <div className='bg-[#F7F7F7] text-[#D6DCE8] flex m-5'>
      <Suspense fallback={<Loader/>}>
        <RecentChats   />
        </Suspense>
        <MainChatCard  />
    </div>
  )
}