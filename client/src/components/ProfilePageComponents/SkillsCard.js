"use client";
import React from 'react'
import { useState } from 'react'

export default function SkillsCard() {
    const [skill, setSkill] = useState(["HTML ","CSS ","JavaScript "])
    const [recommendSkill, setRecommendedSkill] = useState(["ReactJS","Django","Django Rest Framework"])
  return (
    <div className='w-auto bg-white shadow-lg rounded-md p-5 m-5 text-gray-500 h-min border border-gray-200'>
        <div className="my-3 rounded-md p-3 border border-gray-200">
        <h2 className="text-lg lg:text-2xl font-bold">Present Skills</h2>
            {skill.map((item) => (<div className="p-4 text-md lg:text-lg shadow-md my-3 rounded-md border border-gray-200">{item}</div>))}
        </div>
        <div className="my-3 rounded-md p-3 border border-gray-200">
        <h2 className="text-lg lg:text-2xl font-bold">Skills Recommended by Trumio</h2>
            {recommendSkill.map((item) => (<div className="p-4 text-md lg:text-lg shadow-md my-3 rounded-md border border-gray-200">{item}</div>))}
        </div>
    </div>
  )
}
