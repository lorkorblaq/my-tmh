import { useState, useEffect } from 'react';
import CenterListing from './CenterListing';
import Spinner from './Spinner';

const CenterListings = ({ isHome = false }) => {
  const [centers, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchJobs = async () => {
      const apiUrl = isHome ? '/api/tests?_limit=3' : '/api/centers';
      try {
        const res = await fetch(apiUrl);
        const data = await res.json();
        setJobs(data);
      } catch (error) {
        console.log('Error fetching data', error);
      } finally {
        setLoading(false);
      }
    };

    fetchJobs();
  }, []);

  return (
    <section className='bg-blue-50 px-4 py-10'>
      <div className='container-xl lg:container m-auto'>
        <h2 className='text-3xl font-bold text-indigo-500 mb-6 text-center'>
          {isHome ? 'Recent Centers' : 'Browse Centers'}
        </h2>

        {loading ? (
          <Spinner loading={loading} />
        ) : (
          <div className='grid grid-cols-1 md:grid-cols-3 gap-6'>
            {centers.map((center) => (
              <CenterListing key={center.id} center={center} />
            ))}
          </div>
        )}
      </div>
    </section>
  );
};
export default CenterListings;
