'use client'
import React, { useContext } from 'react'
import ProfileCard from '@/components/ProfilePageComponents/ProfileCard'
import SkillsCard from '@/components/ProfilePageComponents/SkillsCard'
import SocialCard from '@/components/ProfilePageComponents/SocialCard'
import ProfileDescriptionCard from '@/components/ProfilePageComponents/ProfileDescriptionCard'
import { useQuery } from '@tanstack/react-query'
import HomeContext from '@/context/HomeContext'
import axios from 'axios'
export default function page() {
  const {auth} = useContext(HomeContext)
  const userDetails = useQuery({
    queryKey:['userProfileDetails'],
    queryFn:()=>{
      return fetchUserDetails(auth.user.id)
    }
  })
  console.log(userDetails)
  if(userDetails.isLoading){
    return <div>Loading...</div>
  }
  return (
    <div className='flex max-md:flex-col'>
      <div className="flex flex-col md:basis-1/3">
        <ProfileCard ele={userDetails}/>
        <SocialCard ele={userDetails}/>
      </div>
      <div className="flex flex-col md:basis-2/3">
        <ProfileDescriptionCard ele={userDetails}/>
        <SkillsCard ele={userDetails}/>
      </div>
      
    </div>
  )
}


const fetchUserDetails = (id) =>{
  return axios.get(`http://127.0.0.1:8000/api/v1/__get__user__data__/${id}`).then((response)=>{
    return response.data
  }).catch((err)=>{
    alert(err)
    console.log(err)
  })
}