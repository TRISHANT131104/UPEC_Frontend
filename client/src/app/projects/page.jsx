// Import necessary dependencies from React and Next.js
'use client'
import React, { Suspense, useContext } from 'react'
import ProjectCard from '@/components/ProjectPageComponents/ProjectCard'
import HomeContext from '@/context/HomeContext'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'

// Define the Projects component
export default function Projects() {
  // Retrieve authentication information from the HomeContext
  const { auth } = useContext(HomeContext)

  // Use React Query to fetch all projects
  const AllProjects = useQuery({
    queryKey:['AllProjects'],
    queryFn:()=>{
      return fetchAllProjects()
    }
  })

  // Use React Query to fetch current projects for the authenticated user
  const CurrentProjects = useQuery({
    queryKey:['CurrentProjects'],
    queryFn:()=>{
      return fetchCurrentProjects(auth.user.id)
    }
  })

  // Render the component
  return (
    <div className='bg-[#F7F7F7] text-[#D6DCE8]'>
      
      {/* Display section for current projects */}
      <div className='shadow-lg m-4 p-4 bg-white rounded-md'>
        <h1 className="text-lg md:text-2xl xl:text-4xl text-slate-500 font-bold">Current Projects</h1>
        {CurrentProjects?.data?.length == 0 ? (
          // Display message if there are no current projects
          <div className="flex flex-col items-center justify-start">
            <img src="noDataFoundGif.3a5ff8c8.gif" alt="" />
            <div className="font-bold text-lg md:text-xl xl:text-3xl text-[#D6DCE8]">No Projects Yet</div>
          </div>
        ) : (
          // Display the list of current projects using ProjectCard component
          <>
            <Suspense fallback={<div>Loading...</div>}>
              {CurrentProjects?.data?.map((ele, index) => {
                return (
                  <div key={index}>
                    <ProjectCard ele={ele} />
                  </div>
                )
              })}
            </Suspense>
          </>
        )}
      </div>

      {/* Display section for recommended projects */}
      <div className='shadow-lg m-4 p-2 md:p-4 bg-white rounded-md'>
        <h1 className="text-lg md:text-2xl xl:text-4xl font-bold text-slate-500">Recommended Projects</h1>
        <Suspense fallback={<div>Loading...</div>}>
          {AllProjects?.data?.map((ele, index) => {
            return (
              <div key={index}>
                <ProjectCard ele={ele} />
              </div>
            )
          })}
        </Suspense>
      </div>

    </div>
  )
}

// Function to fetch all projects
const fetchAllProjects = async () => {
  return axios.get(`http://103.159.214.229/api/v1/__get__all__projects__`).then((response)=>{
    return response.data
  }).catch((err)=>{
    alert(err)
  })
}

// Function to fetch current projects for a specific user
const fetchCurrentProjects = async (id) => {
  return axios.get(`http://103.159.214.229/api/v1/__get__users__ongoing__projects__/${id}`).then((response)=>{
    return response.data
  }).catch((err)=>{
    alert(err)
  })
}

