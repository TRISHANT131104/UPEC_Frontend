"use client";
import React from 'react'
import { useState } from 'react';

export default function SocialCard() {
    const [socialLinks, setSocialLinks] = useState({
        Github: "github.com",
        Linkedin: "linkedin.com",
        Twitter: "twitter.com"
      });
  return (
    <div className="m-5">
        <div className="p-3 w-auto shadow-lg bg-white rounded-md border border-gray-200 text-center">
            <h1 className="text-lg lg:text-2xl text-gray-500 font-bold">Social</h1>
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
