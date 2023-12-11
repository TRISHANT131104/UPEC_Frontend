"use client";
import React, { useEffect } from 'react'
import { useState } from 'react'

export default function SkillsCard({ele}) {
  
  
  return (
    <div className='w-auto card m-5 h-min'>
        <div className="my-3 rounded-md p-3 border border-gray-200">
        <h2 className="titleCard">Present Skills</h2>
            {ele?.data?.skills?.map((item,index) => {
              return (<div key={index} className="p-4 my-3 bodyCard border border-gray-200 shadow-md">{item}</div>)
            })}
        </div>
        <div className="my-3 rounded-md p-3 border border-gray-200">
            <h2 className="titleCard">Skills Recommended by Trumio</h2>
            {ele?.data?.learning_resources?.map((ele,index) => {
              return (
                <div key={index}>
                <div onClick={()=>{
                  window.location.href = ele.url
                }} className="p-4 my-3 bodyCard border border-gray-200 shadow-md">{ele.title}</div>
                </div>
              )
            
            }
            )}
        </div>
    </div>
  )
}
