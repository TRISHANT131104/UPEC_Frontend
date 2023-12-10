'use client'
import { Inter } from 'next/font/google'
import './globals.css'
import React from 'react'
import NavbarComponent from '@/components/NavbarComponent/NavbarComponent'
import {
  useQuery,
  useMutation,
  useQueryClient,
  Hydrate,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import HomeContext, { HomeProvider } from '@/context/HomeContext'
const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({ children }) {
  const [queryClient] = React.useState(() => new QueryClient())
  return (

    <html lang="en">
      <body className={inter.className}>

        <QueryClientProvider client={queryClient}>
          <HomeProvider>
            <NavbarComponent />
            {children}

            
          </HomeProvider>
          
        </QueryClientProvider>

      </body>
    </html>

  )
}
