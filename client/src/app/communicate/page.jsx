'use client'
import React, { useContext, useState } from 'react'
import RecentChats from '@/components/CommunicatePageComponents/RecentChats'
import MainChatCard from '@/components/CommunicatePageComponents/MainChatCard'
import HomeContext from '@/context/HomeContext'

export default function Projects() {
  const {EachUsersMessage,setEachUserMessage,auth} = useContext(HomeContext)
  
  return (
    <div className='bg-[#F7F7F7] text-[#D6DCE8] flex m-5'>
        <RecentChats   />
        <MainChatCard  />
    </div>
  )
}