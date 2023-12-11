"use client";
import React from 'react'
import { useState } from 'react'

export default function ProfileDescriptionCard({ele}) {
  const [role, setRole] = useState("Web Developer")
  const [projectDescription, setProjectDescription] = useState("Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti beatae expedita eaque aspernatur natus quae omnis eum temporibus quod iste, nulla molestiae provident deserunt, cum numquam inventore asperiores nam exercitationem!")
  const [experience, setExperience] = useState("3 Years, 6 Months")
  return (
    <div className='m-5'>
      <div className="w-auto border border-gray-200 rounded-md card">
        <div className="w-full text-center headingCard">About</div>
        <div className="card !p-4 shadow-md my-4">
          <div className="titleTextDiv">Role:</div>
          <div className="bodyTextDiv">{ele?.data?.role}</div>
        </div>
        <div className="card !p-4 shadow-md my-4">
          <div className="titleTextDiv">Experience:</div>
          <div className="bodyTextDiv">{experience}</div>
        </div>
        <div className="card !p-4 shadow-md my-4">
          <div className="titleTextDiv">Profile Description:</div>
          <div className="bodyTextDiv">{projectDescription}</div>
        </div>
      </div>
    </div>
  )
}
