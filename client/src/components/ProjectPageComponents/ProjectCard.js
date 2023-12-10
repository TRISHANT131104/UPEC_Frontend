'use client'
import React, { useState } from 'react'
import WorkflowCard from './WorkflowCard'
import sampleData from './sampleData.json'
import Link from 'next/link'
export default function ProjectCard({ele}) {

  const [open, setOpen] = useState(false);
  const [workflowData, setWorkflowData] = useState({});

  const closeWorkflow = () => {
    setWorkflowData({})
    setOpen(false)
    console.log("Close Workflow")
  }
  const handleGenerateWorkflow = async () => {
    setOpen(true)
    try {
      // Perform the API request to generate the workflow
      // const response = await fetch(`/api/generateWorkflow?id=${projectId}`);
      // get response from the sampleResponse.json file
      const response = sampleData['data'];

      // Set the response data to the state
      setWorkflowData(response);
      console.log(response)
    } catch (error) {
      console.error('Error generating workflow:', error);
    }
  };
  return (
    <>
      <div className="bg-white rounded-md shadow-lg m-4 sm:m-4 w-[98%]">
        <div className="flex p-2 md:p-4 w-full">
          <div className="flex-col text-[#414141] m-4 w-full">
            <span className='text-sm md:text-md bg-[#28C76F] bg-opacity-10 text-[#28C76F] px-3 py-2 rounded-xl font-bold'>{ele.status}</span>
            <p className="pt-4 text-md md:text-lg xl:text-2xl font-bold">{ele.title}</p>
            <div className="text-xs md:text-sm md:text-md hidden sm:flex justify-start my-1">
              <div className="mr-2">Variable Price {ele.bid_price}</div>
              <div className="mr-2">United States</div>
              <div className="mr-2">Posted On {ele.created_at}</div>
            </div>
            <p className="hidden md:block pr-4 my-4 text-sm text-left">{ele.description.slice(0,200)}...</p>
            <div className="py-3 sm:py-2 flex">
              <div className="flex items-center gap-2">
                <div className="flex-shrink-0">
                  <img className="w-8 h-8 rounded-full" src="https://www.gravatar.com/avatar/2acfb745ecf9d4dccb3364752d17f65f?s=260&d=mp" alt="Neil image" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium text-[#5E5873] truncate">
                    {ele?.created_by?.user?.username}
                  </p>
                  <p className="text-sm text-[#5E5873] truncate">
                    {ele?.created_by?.user?.email}
                  </p>
                </div>
                <div class="flex items-center bg-[#FFEDE0] p-2 rounded-lg">
                  <svg class=" h-3 w-3 md:w-4 md:h-4 text-[#FF9F43] md:me-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 20">
                    <path d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
                  </svg>
                  <p class="ms-2 text-xs md:text-sm font-bold text-[#928F8B]">{ele?.created_by?.rating}</p>
                </div>
              </div>
            </div>
            <div className="flex justify-between items-center text-bold">
              <div className="">
                Skills
                <div className="flex gap-x-2 flex-wrap">
                  {ele?.related_techstacks.map((item,index)=>{
                    return(
                      <div key={index}>
                        <div className="bg-[#E3F2FD] text-[#3EA4F4] text-sm font-normal py-1 my-1 px-2 rounded-lg">{item}</div>
                        
                      </div>
                    )
                  })}
                  
                </div>
              </div>  
                <Link href={`/projects/${ele.id}`} className="cursor-pointer hidden sm:block text-sm md:text-md bg-[#28C76F] hover:bg-[#3cad6f] bg-opacity-80 text-white px-3 py-2 rounded-md font-bold h-min">Know More</Link>
              
            </div>
            <div className='flex sm:hidden pt-3 justify-end'>
                <Link href={`/projects/${ele.id}`} className="cursor-pointer sm:hidden text-sm md:text-md bg-[#28C76F] hover:bg-[#3cad6f] bg-opacity-80 text-white px-3 py-2 rounded-md font-bold h-min">Know More</Link>
            </div>
            {workflowData && open && <WorkflowCard workflowData={workflowData}/>}
          </div>
        </div>
      </div>
    </>
  )
}
