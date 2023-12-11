"use client";
import React from 'react'
import Link from 'next/link'
import { useState } from 'react';

export default function ProfileCard({ele}) {
    
    const [image, setImage] = useState("https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp");
    const [institute, setInstitute] = useState("Indian Institute of Technology")
    const [mobile_no, setMobile_no] = useState("+977 9955221114")
    
  return (
<div className="hidden lg:flex justify-center w-1/5 lg:w-1/4">
<div className="">
    <div className="card">
        <div className="photo-wrapper p-2">
        <img className="w-16 h-16 lg:w-24 lg:h-24 xl:w-32 xl:h-32 rounded-full mx-auto" src={image} alt={ele?.data?.username}/>
        </div>
        <div className="p-2">
            <h3 className="text-center titleTextDiv">{ele?.data?.username}</h3>
            <div className="text-center bodyTextDiv">
                <p>{ele?.data?.role}</p>
            </div>
            <div className="flex justify-center">
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

            <table className="text-xs my-3 bodyTextDiv">
                <tbody><tr>
                    <td className="px-2 py-2 titleTextDiv">Institution</td>
                    <td className="px-2 py-2">{institute}</td>
                </tr>
                <tr>
                    <td className="px-2 py-2 titleTextDiv">Phone</td>
                    <td className="px-2 py-2">{mobile_no}</td>
                </tr>
                <tr>
                    <td className="px-2 py-2 titleTextDiv">Email</td>
                    <td className="px-2 py-2">{ele?.data?.email}</td>
                </tr>
                <tr>
                    <td className="px-2 py-2 titleTextDiv">Skills</td>
                    <div className='flex flex-wrap'>
                    {ele?.data?.skills?.map((ele,index)=>(<div key={index} className="px-2 py-2">{ele}</div>))}
                    </div>
                    
                </tr>
            </tbody></table>

            <div className="text-center my-3">
                <Link className="text-xs text-indigo-500 italic hover:underline hover:text-indigo-600 font-medium" href="https://linkedin.com" target="_blank">View Profile</Link>
            </div>

        </div>
    </div>
</div>

</div>
  )
}


// SAMPLE JSON DATA FOR PROFILE
// {
//     "firstName":{
//        "localized":{
//           "en_US":"Bob"
//        },
//        "preferredLocale":{
//           "country":"US",
//           "language":"en"
//        }
//     },
//     "localizedFirstName": "Bob",
//     "headline":{
//        "localized":{
//           "en_US":"API Enthusiast at LinkedIn"
//        },
//        "preferredLocale":{
//           "country":"US",
//           "language":"en"
//        }
//     },
//     "localizedHeadline": "API Enthusiast at LinkedIn",
//     "vanityName": "bsmith",
//     "id":"yrZCpj2Z12",
//     "lastName":{
//        "localized":{
//           "en_US":"Smith"
//        },
//        "preferredLocale":{
//           "country":"US",
//           "language":"en"
//        }
//     },
//     "localizedLastName": "Smith",
//     "profilePicture": {
//          "displayImage": "urn:li:digitalmediaAsset:C4D00AAAAbBCDEFGhiJ"
//     }
//  }