import { useState, useEffect } from 'react';
import TestListing from './TestListing';
import Spinner from './Spinner';

const TestListings = ({ isHome = false }) => {
  const [tests, setTests] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTests = async () => {
      const apiUrl = isHome ? '/api/tests?_limit=3' : '/api/tests';
      try {
        const res = await fetch(apiUrl);
        const data = await res.json();
        setTests(data);
      } catch (error) {
        console.log('Error fetching data', error);
      } finally {
        setLoading(false);
      }
    };

    fetchTests();
  }, []);

  return (
    <section className='bg-blue-50 px-4 py-10'>
      <div className='container-xl lg:container m-auto'>
        <h2 className='text-3xl font-bold text-indigo-500 mb-6 text-center'>
          {isHome ? 'Recent Tests' : 'Browse Tests'}
        </h2>

        {loading ? (
          <Spinner loading={loading} />
        ) : (
          <div className='grid grid-cols-1 md:grid-cols-3 gap-6'>
            {tests.map((test) => (
              <TestListing key={test.id} test={test} />
            ))}
          </div>
        )}
      </div>
    </section>
  );
};
export default TestListings;
