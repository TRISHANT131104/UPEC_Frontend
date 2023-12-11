"use client";
import React, { useEffect } from 'react'
import { useState } from 'react'

export default function SkillsCard({ele}) {
  
  
  return (
    <div className='w-auto bg-white shadow-lg rounded-md p-5 m-5 text-gray-500 h-min border border-gray-200'>
        <div className="my-3 rounded-md p-3 border border-gray-200">
        <h2 className="text-lg lg:text-2xl font-bold">Present Skills</h2>
            {ele?.data?.skills?.map((item,index) => {
              return (<div key={index} className="p-4 text-md lg:text-lg shadow-md my-3 rounded-md border border-gray-200">{item}</div>)
            })}
        </div>
        <div className="my-3 rounded-md p-3 border border-gray-200">
            <h2 className="text-lg lg:text-2xl font-bold">Skills Recommended by Trumio</h2>
            {ele?.data?.learning_resources?.map((ele,index) => {
              return (
                <div key={index}>
                <div onClick={()=>{
                  window.location.href = ele.url
                }} className="p-4 text-md lg:text-lg shadow-md my-3 rounded-md border border-gray-200">{ele.title}</div>
                </div>
              )
            
            }
            )}
        </div>
    </div>
  )
}
