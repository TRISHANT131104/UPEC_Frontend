import React, { Suspense } from 'react'
import ProjectCard from '@/components/ProjectPageComponents/ProjectCard'

export default async function Projects() {
  const AllProjects = await fetchAllProjects()
  console.log(AllProjects)
  return (
    <div className='bg-[#F7F7F7] text-[#D6DCE8]'>
      <Suspense fallback={<div>Loading...</div>}>
      <div className='shadow-lg m-4 p-4 bg-white rounded-md'>
        <h1 className="text-lg md:text-2xl xl:text-4xl font-bold">Current Projects</h1>
        <div className="flex flex-col items-center justify-start">
          <img src="noDataFoundGif.3a5ff8c8.gif" alt="" />
          <div className="font-bold text-lg md:text-xl xl:text-3xl text-[#D6DCE8]">No Projects Yet</div>
        </div>
      </div>
      <div className='shadow-lg m-4 p-2 md:p-4 bg-white rounded-md'>
        <h1 className="text-lg md:text-2xl xl:text-4xl font-bold">Recommended Projects</h1>
        {AllProjects.map((ele,index)=>{
          return (
            <ProjectCard ele={ele}/>
          )
        })}
        
      </div>
      </Suspense>
    </div>
  )
}

const fetchAllProjects = async () =>{
  const res = await fetch('http://127.0.0.1:8000/api/v1/__get__all__projects__')
  const json = await res.json()
  console.log('json',json)
  return json
}