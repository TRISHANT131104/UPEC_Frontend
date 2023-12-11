'use client'
import { useQuery } from '@tanstack/react-query'
import { useRouter } from 'next/navigation'
import React, { useState, useContext } from 'react'
import axios from 'axios'
import EachProjectCard from '@/components/ProjectPageComponents/EachProjectCard'
import WorkflowCard from '@/components/ProjectPageComponents/WorkflowCard'
import parse from 'html-react-parser';
import PRDCard from '@/components/ProjectPageComponents/PRDCard'
import HomeContext from '@/context/HomeContext'
import ReactModal from 'react-modal'
import Loader from '@/components/Loader'
import toast, { Toaster } from 'react-hot-toast';
import { ClipLoader } from 'react-spinners'
export default function EachProject({ params }) {
    const [workflowOpen, setWorkflowOpen] = useState(false)
    const [learningResourcesOpen, setlearningResourcesOpen] = useState(false)
    const [prdOpen, setPrdOpen] = useState(false)
    const [projectManagementOpen, setProjectManagementOpen] = useState(false)
    const workflowClick = () => {
        setWorkflowOpen(prevState => !prevState);
    };
    const learningResourcesClick = () => {
        setlearningResourcesOpen(prevState => !prevState);
    };
    const prdClick = () => {
        setPrdOpen(prevState => !prevState);
    };
    const projectManagementClick = () => {
        setProjectManagementOpen(prevState => !prevState);
    };
    console.log(params)
    const { auth } = useContext(HomeContext)
    const router = useRouter()
    console.log(router)
    const EachProject = useQuery({
        queryKey: ["EachProject"],
        queryFn: () => {
            return fetchEachProject(params.id)
        }
    })
    console.log(EachProject)
    const customStyles = {
        overlay: {
            position: "fixed",
            zIndex: 1020,
            top: 0,
            left: 0,
            width: "100vw",
            height: "100vh",
            background: "rgba(0, 0, 0, 0.75)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
        },
        content: {
            top: "50%",
            left: "50%",
            height: "fit-content",
            width: '80%',
            transform: "translate(-50%, -50%)",
            background: "transparent",
            overflow: "hidden",
            border: "0px",
        },
    };

    const [modalIsOpen, setIsOpen] = React.useState(false);
    return (
        <div>
            
            <ReactModal
                isOpen={modalIsOpen}
                style={customStyles}
                contentLabel="Example Modal"
            >
                <div className='w-full text-center flex justify-center  items-center'>
                    <ClipLoader color={"white"}
                        size={100}
                        aria-label="Loading Spinner"
                        data-testid="loader" />
                </div>
            </ReactModal>
            <section className="bg-[#F7F7F7] text-gray-600 body-font">
                <div className="container justify-center flex px-5 py-20 md:flex-row flex-col items-center">
                    <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
                        <EachProjectCard ele={EachProject?.data} />
                    </div>
                    <div className="lg:flex-grow md:w-1/2 m-5 p-5 flex flex-col md:items-start md:text-left items-center text-center bg-white shadow-lg rounded-md">
                        <h1 className="title-font sm:text-3xl text-xl mb-4 font-medium text-gray-500">{EachProject?.data?.title}
                        </h1>
                        <p className="mb-8 leading-relaxed">{EachProject?.data?.description}</p>
                        {(EachProject?.data?.created_by?.user?.id != auth.user.id) ? (
                            <>
                                {(EachProject?.data?.status != "Open" && EachProject?.data?.team?.members?.some((x) => x.id === auth.user.id)) && (
                                    <div className="grid grid-cols-2 justify-center text-center">
                                        <>
                                            {(EachProject?.data?.workflow === null) && (
                                                <button className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 text-center flex justify-center items-center" onClick={() => {
                                                    setIsOpen(true)
                                                    axios.post('http://103.159.214.229/api/v1/__send__generated__workflow__/', { id: auth.user.id, project_id: EachProject?.data?.id }).then((response) => {
                                                        EachProject.refetch()
                                                        console.log(response.data)
                                                        setIsOpen(false)
                                                        toast('WorkFlow generated')
                                                    }).catch((Err) => {
                                                        setIsOpen(false)
                                                        toast('try again')
                                                    })
                                                }}>Generate Workflow</button>
                                            )}
                                            {(EachProject?.data?.Learning_resources == null || EachProject?.data?.Learning_resources?.length == 0) && (
                                                <button onClick={() => {
                                                    setIsOpen(true)
                                                    axios.post('http://103.159.214.229/api/v1/__learning__resource__/', { id: auth.user.id, project_id: EachProject?.data?.id }).then((response) => {
                                                        EachProject.refetch()
                                                        console.log(response.data)
                                                        setIsOpen(false)
                                                        toast('Learning Resources generated')
                                                    }).catch((Err) => {
                                                        setIsOpen(false)
                                                        toast('try again')
                                                    })
                                                }} className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 text-center flex justify-center items-center">Generate Learning Resources</button>
                                            )}
                                            {(EachProject?.data?.prd != null && (EachProject?.data?.project_management == null || EachProject?.data?.project_management.length == 0 || EachProject?.data?.project_management == "")) && (
                                                <button onClick={() => {
                                                    setIsOpen(true)
                                                    axios.post('http://103.159.214.229/api/v1/__project__management__/', { id: auth.user.id, project_id: EachProject?.data?.id }).then((response) => {
                                                        EachProject.refetch()
                                                        console.log(response.data)
                                                        setIsOpen(false)
                                                        toast('Project Management generated')
                                                    }).catch((Err) => {
                                                        setIsOpen(false)
                                                        toast('try again')
                                                    })
                                                }} className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 items-center">Generate Project Mangement</button>
                                            )}
                                        </>
                                    </div>
                                )}
                            </>
                        ) : (

                            <div className="grid grid-cols-2 justify-center text-center">
                                <>
                                    {EachProject?.data?.prd == null && (
                                        <button onClick={() => {
                                            setIsOpen(true)
                                            axios.post('http://103.159.214.229/api/v1/__send__generated__prd__/', { id: auth.user.id, project_id: EachProject?.data?.id }).then((response) => {
                                                EachProject.refetch()
                                                console.log(response.data)
                                                setIsOpen(false)
                                                toast('PRD generated')
                                            }).catch((Err) => {
                                                setIsOpen(false)
                                                toast('try again')
                                            })
                                        }} className=" text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg m-5 items-center">Generate PRD</button>
                                    )}
                                </>
                            </div>

                        )}

                    </div>
                </div>
                {EachProject?.data?.workflow && (
                    <div className='mx-10 my-10 text-black'>
                        <div onClick={workflowClick} className="flex my-5 items-center justify-between bg-white rounded-md shadow-lg p-2 px-5 hover:bg-[#E9F3FF] hover:border hover:border-blue-500 text-gray-500 hover:text-gray-800">
                            <h1 className='text-center font-semibold text-lg md:text-xl lg:text-3xl px-5'>Workflow For Talents </h1>
                            <div className="">
                                {workflowOpen ? (
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="40" height="40" class="text-gray-500">
                                        <circle cx="12" cy="12" r="9" fill="none" stroke="black" strokeWidth="2" />
                                        <path d="M 7 12 H 17" fill="none" stroke="black" strokeWidth="2" />
                                    </svg>
                                ) : (
                                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="40" height="40" viewBox="0 0 24 24" class="text-gray-500">
                                        <path d="M 12 2 C 6.4889971 2 2 6.4889971 2 12 C 2 17.511003 6.4889971 22 12 22 C 17.511003 22 22 17.511003 22 12 C 22 6.4889971 17.511003 2 12 2 z M 12 4 C 16.430123 4 20 7.5698774 20 12 C 20 16.430123 16.430123 20 12 20 C 7.5698774 20 4 16.430123 4 12 C 4 7.5698774 7.5698774 4 12 4 z M 11 7 L 11 11 L 7 11 L 7 13 L 11 13 L 11 17 L 13 17 L 13 13 L 17 13 L 17 11 L 13 11 L 13 7 L 11 7 z"></path>
                                    </svg>
                                )}
                            </div>
                        </div>
                        {workflowOpen ? (
                            <div className='bg-white p-10 shadow-lg rounded-md text-gray-500'>
                                {EachProject.isSuccess ? parse(EachProject.data.workflow ? EachProject.data.workflow.description : "") : ""}
                            </div>
                        ) : ("")}
                    </div>
                )}

                {EachProject?.data?.Learning_resources && (
                    <div className='mx-10 my-10'>
                        <div onClick={learningResourcesClick} className="flex my-5 items-center justify-between bg-white rounded-md shadow-lg p-2 px-5 hover:bg-[#E9F3FF] hover:border hover:border-blue-500 text-gray-500 hover:text-gray-800">
                            <h1 className='text-center font-semibold px-5 text-lg md:text-xl lg:text-3xl'>Learning Resources For Talents</h1>
                            <div className="">
                                {learningResourcesOpen ? (
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="40" height="40" class="text-gray-500">
                                        <circle cx="12" cy="12" r="9" fill="none" stroke="black" strokeWidth="2" />
                                        <path d="M 7 12 H 17" fill="none" stroke="black" strokeWidth="2" />
                                    </svg>
                                ) : (
                                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="40" height="40" viewBox="0 0 24 24" class="text-gray-500">
                                        <path d="M 12 2 C 6.4889971 2 2 6.4889971 2 12 C 2 17.511003 6.4889971 22 12 22 C 17.511003 22 22 17.511003 22 12 C 22 6.4889971 17.511003 2 12 2 z M 12 4 C 16.430123 4 20 7.5698774 20 12 C 20 16.430123 16.430123 20 12 20 C 7.5698774 20 4 16.430123 4 12 C 4 7.5698774 7.5698774 4 12 4 z M 11 7 L 11 11 L 7 11 L 7 13 L 11 13 L 11 17 L 13 17 L 13 13 L 17 13 L 17 11 L 13 11 L 13 7 L 11 7 z"></path>
                                    </svg>
                                )}
                            </div>
                        </div>
                        {learningResourcesOpen ? (
                            <div className='bg-white p-10 shadow-lg rounded-md text-gray-500' id="learning_resources">
                                {EachProject.isSuccess ? parse(EachProject.data.Learning_resources ? EachProject.data.Learning_resources : "") : ""}
                            </div>
                        ) : ("")}
                    </div>
                )}

                {EachProject?.data?.prd && (
                    <div className='mx-10 my-10'>
                        <div onClick={prdClick} className="flex my-5 items-center justify-between bg-white rounded-md shadow-lg p-2 px-5 hover:bg-[#E9F3FF] hover:border hover:border-blue-500 text-gray-500 hover:text-gray-800">
                            <h1 className='text-center font-semibold px-5 text-lg md:text-xl lg:text-3xl'>Project Requirement Document</h1>
                            <div className="">
                                {prdOpen ? (
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="40" height="40" class="text-gray-500">
                                        <circle cx="12" cy="12" r="9" fill="none" stroke="black" strokeWidth="2" />
                                        <path d="M 7 12 H 17" fill="none" stroke="black" strokeWidth="2" />
                                    </svg>
                                ) : (
                                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="40" height="40" viewBox="0 0 24 24" class="text-gray-500">
                                        <path d="M 12 2 C 6.4889971 2 2 6.4889971 2 12 C 2 17.511003 6.4889971 22 12 22 C 17.511003 22 22 17.511003 22 12 C 22 6.4889971 17.511003 2 12 2 z M 12 4 C 16.430123 4 20 7.5698774 20 12 C 20 16.430123 16.430123 20 12 20 C 7.5698774 20 4 16.430123 4 12 C 4 7.5698774 7.5698774 4 12 4 z M 11 7 L 11 11 L 7 11 L 7 13 L 11 13 L 11 17 L 13 17 L 13 13 L 17 13 L 17 11 L 13 11 L 13 7 L 11 7 z"></path>
                                    </svg>
                                )}
                            </div>
                        </div>
                        {prdOpen ? (
                            <div className='grid grid-cols-1 justify-center bg-white p-10 shadow-lg rounded-md text-gray-500'>
                                {["project_overview", "original_requirements", "project_goals", "user_stories", "system_architecture", "tech_stacks", "requirement_pool", "ui_ux_design", "development_methodology", "security_measures", "testing_strategy", "scalability_and_performance", "deployment_plan", "maintenance_and_support", "risks_and_mitigations", "compliance_and_regulations", "budget_and_resources", "timeline_and_milestones", "communication_plan", "anything_unclear"].map((ele, index) => (
                                    <div key={index} className='my-5'>
                                        <PRDCard key={index} ele={ele} EachProject={EachProject} />
                                    </div>
                                ))}
                            </div>
                        ) : ("")}
                    </div>
                )}

                {EachProject?.data?.project_management && (
                    <div className='mx-10 my-10'>
                        <div onClick={projectManagementClick} className="flex my-5 items-center justify-between bg-white rounded-md shadow-lg p-2 px-5 hover:bg-[#E9F3FF] hover:border hover:border-blue-500 text-gray-500 hover:text-gray-800">
                            <h1 className='text-center font-semibold px-5 text-lg md:text-xl lg:text-3xl'>Project Management</h1>
                            <div className="">
                                {projectManagementOpen ? (
                                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="40" height="40" class="text-gray-500">
                                        <circle cx="12" cy="12" r="9" fill="none" stroke="black" strokeWidth="2" />
                                        <path d="M 7 12 H 17" fill="none" stroke="black" strokeWidth="2" />
                                    </svg>
                                ) : (
                                    <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="40" height="40" viewBox="0 0 24 24" class="text-gray-500">
                                        <path d="M 12 2 C 6.4889971 2 2 6.4889971 2 12 C 2 17.511003 6.4889971 22 12 22 C 17.511003 22 22 17.511003 22 12 C 22 6.4889971 17.511003 2 12 2 z M 12 4 C 16.430123 4 20 7.5698774 20 12 C 20 16.430123 16.430123 20 12 20 C 7.5698774 20 4 16.430123 4 12 C 4 7.5698774 7.5698774 4 12 4 z M 11 7 L 11 11 L 7 11 L 7 13 L 11 13 L 11 17 L 13 17 L 13 13 L 17 13 L 17 11 L 13 11 L 13 7 L 11 7 z"></path>
                                    </svg>
                                )}
                            </div>
                        </div>
                        {projectManagementOpen ? (
                            <div className='grid grid-cols-1 justify-center bg-white p-10 shadow-lg rounded-md text-gray-500'>
                                <WorkflowCard workflowData={EachProject?.data?.project_management} />
                                { }
                            </div>
                        ) : ("")}
                    </div>
                )}



            </section>
            <style jsx>
                {`
                 #learning_resources  a{
                    color:blue;
                    margin:10px 10px;
                 }
                `}
            </style>
        </div>
    )
}


const fetchEachProject = async (id) => {
    return axios.get(`http://103.159.214.229/api/v1/__get__each__project__/${id}`).then((response) => {
        return response.data
    }).catch((error) => {
        return []
    })
}
