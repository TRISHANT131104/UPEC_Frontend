import React from 'react'
import ProfileCard from '@/components/ProfilePageComponents/ProfileCard'
import SkillsCard from '@/components/ProfilePageComponents/SkillsCard'
import SocialCard from '@/components/ProfilePageComponents/SocialCard'
import ProfileDescriptionCard from '@/components/ProfilePageComponents/ProfileDescriptionCard'

export default function page() {
  return (
    <div className='flex max-md:flex-col'>
      <div className="flex flex-col md:basis-1/3">
        <ProfileCard/>
        <SocialCard/>
      </div>
      <div className="flex flex-col md:basis-2/3">
        <ProfileDescriptionCard/>
        <SkillsCard/>
      </div>
      
    </div>
  )
}
