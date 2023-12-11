"use client";
import React from 'react'
import { useState } from 'react';

export default function ProfileCard({ele}) {
    const [image, setImage] = useState("https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp");
    const [institute, setInstitute] = useState("Indian Institute of Technology")
    const [mobile_no, setMobile_no] = useState("+977 9955221114")
    const [socialLinks, setSocialLinks] = useState({
      Github: "github.com",
      Linkedin: "linkedin.com",
      Twitter: "twitter.com"
    });
    
  return (
<div className="flex justify-center w-full">
    <div className="w-auto m-5 border border-gray-200 h-min card">
        <div className="photo-wrapper p-2">
        <img className="w-16 h-16 lg:w-24 lg:h-24 xl:w-32 xl:h-32 rounded-full mx-auto" src={image} alt={ele?.data?.username}/>
        </div>
        <div className="py-2 px-4 flex flex-col items-center justify-center">
            <h3 className="text-center titleTextDiv leading-8">{ele?.data?.username}</h3>
            <div className="text-center text-md lg:text-lg text-gray-400 font-semibold mb-2">
                <p><span className='bg-gray-200 rounded-md px-2 py-1'>{ele?.data?.role}</span></p>
            </div>
            <div className="flex mb-2">
                <svg className="w-4 h-4 text-yellow-300 me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                </svg>
                <svg className="w-4 h-4 text-yellow-300 me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                </svg>
                <svg className="w-4 h-4 text-yellow-300 me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                </svg>
                <svg className="w-4 h-4 text-yellow-300 me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                </svg>
                <svg className="w-4 h-4 text-gray-300 me-1 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z"/>
                </svg>
                <p className="ms-1 bodyTextDiv">{ele?.data?.rating}</p>
                <p className="ms-1 bodyTextDiv">out of</p>
                <p className="ms-1 bodyTextDiv">5</p>
            </div>

            <table className="text-md lg:text-lg my-2">
                <tbody>
                    <tr>
                        <td className="px-2 lg:p-2 titleTextDiv">Institution</td>
                        <td className="px-2 lg:p-2 bodyTextDiv">{institute}</td>
                    </tr>
                    <tr>
                        <td className="px-2 lg:p-2 titleTextDiv">Phone</td>
                        <td className="px-2 lg:p-2 bodyTextDiv">{mobile_no}</td>
                    </tr>
                    <tr>
                        <td className="px-2 lg:p-2 titleTextDiv">Email</td>
                        <td className="px-2 lg:p-2 bodyTextDiv">{ele?.data?.email}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
  )
}