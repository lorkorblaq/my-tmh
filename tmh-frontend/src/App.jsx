import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from 'react-router-dom';
import MainLayout from './layouts/MainLayout';
import HomePage from './pages/HomePage';

import TestPage, { testLoader } from './pages/TestPage';
import TestsPage from './pages/TestsPage';

import CenterPage, { centerLoader } from './pages/CenterPage';
import CentersPage from './pages/CentersPage';

import HMOPage, { HMOLoader } from './pages/HMOPage';
import HMOsPage from './pages/HMOsPage';

import NotFoundPage from './pages/NotFoundPage';

import AppointementPage from './pages/AppointementPage';
import EditUser from './pages/EditUser';

const App = () => {
  // Add New Job
  const addAppointment = async (newAppointment) => {
    const res = await fetch('/api/appointment', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newAppointment),
    });
    return;
  };

  // Delete Job
  const deleteJob = async (id) => {
    const res = await fetch(`/api/test/${id}`, {
      method: 'DELETE',
    });
    return;
  };

  // Update Job
  const updateJob = async (test) => {
    const res = await fetch(`/api/test/${test.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(test),
    });
    return;
  };

  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path='/' element={<MainLayout />}>
        <Route index element={<HomePage />} />
        <Route path='/tests' element={<TestsPage />} />
        <Route path='/centers' element={<CentersPage />} />
        <Route path='/hmos' element={<HMOsPage />} />

        <Route path='/appointments' element={<AppointementPage addAppointmentSubmit={addAppointment} />} />
        <Route
          path='/edit-job/:id'
          element={<EditUser updateJobSubmit={updateJob} />}
          loader={testLoader}
        />
        <Route
          path='/test/:id'
          element={<TestPage deleteJob={deleteJob} />}
          loader={testLoader}
        />
        <Route
          path='/center/:id'
          element={<CenterPage deleteJob={deleteJob} />}
          loader={centerLoader}
        />
        <Route
          path='/center/:id'
          element={<HMOPage deleteJob={deleteJob} />}
          loader={HMOLoader}
        />
        <Route path='*' element={<NotFoundPage />} />
      </Route>
    )
  );

  return <RouterProvider router={router} />;
};
export default App;
