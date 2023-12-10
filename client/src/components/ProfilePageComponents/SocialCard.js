"use client";
import React from 'react'
import { useState } from 'react';

export default function SocialCard({ele}) {
    const [socialLinks, setSocialLinks] = useState({
        "Projects Completed": ele?.data?.no_projects_completed,
        "Deadline Missed": ele?.data?.deadline_missed,
        "Project Cancelled": ele?.data?.project_cancelled
      });
  return (
    <div className="m-5">
        <div className="p-3 w-auto shadow-lg bg-white rounded-md border border-gray-200 text-center">
            <h1 className="text-lg lg:text-2xl text-gray-500 font-bold">Stats</h1>
            <div className="text-start text-gray-500">
                {Object.entries(socialLinks).map(([platform, link]) => (
                <div key={platform} className='text-md lg:text-lg'>
                    <strong>{platform}:</strong> <a href={`https://${link}`} target="_blank" rel="noopener noreferrer">{link}</a>
                </div>
                ))}
            </div>
        </div>
    </div>
  )
}
