"use client";
import React from 'react'
import { useState } from 'react';

export default function StatsCard({ele}) {
    const [socialLinks, setSocialLinks] = useState({
        "Projects Completed": ele?.data?.no_projects_completed,
        "Deadline Missed": ele?.data?.deadline_missed,
        "Project Cancelled": ele?.data?.project_cancelled});
  return (
    <div className="m-5">
        <div className="border border-gray-200 text-center card w-auto">
            <h1 className="headingCard">Stats</h1>
            <div className="text-start">
                {Object.entries(socialLinks).map(([platform, link]) => (
                <div key={platform}>
                    {/* <div className='border-1 border-gray-500 rounded-md py-1'> */}
                    <div className='px-2 lg:p-2 titleTextDiv inline'>{platform}:</div> <a href={`https://${link}`} target="_blank" rel="noopener noreferrer" className='bodyTextDiv inline'>{link}</a>
                    {/* </div> */}
                </div>
                ))}
            </div>
        </div>
    </div>
  )
}
